from django.http import JsonResponse
from django.shortcuts import render
from .models import CodeFile
from . import services
import os
from code_check.settings import BASE_DIR
from pygments import highlight
from django.views.decorators.csrf import csrf_exempt
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter

def upload_page(request):
    '''страница загрузки файлов'''
    list_of_files = CodeFile.objects.filter(user = request.user)
    context = {'list_of_files':list_of_files}
    return render(request, 'upload_page.html',context)

def show_file(request,file_id):
    '''получение содержимого файла по id'''
    file = CodeFile.objects.get(id = file_id)
    path = os.path.join(BASE_DIR,f'{file.file}')
    with open(path, 'r') as file:
        code_content = file.read()
    formatted_code = highlight(code_content, PythonLexer(), HtmlFormatter())
    return JsonResponse({'file':formatted_code,'file_id':file_id})

def upload_file(request):
    '''загрузка файла'''
    if request.method == 'POST':
        res = services.upload_file(request)
        if res:
            return JsonResponse({'success': True,'data':res})
        else:
            return JsonResponse({'success': False, 'error': 'Invalid file format.'})

def delete_file(request, file_id):
    '''удаление файла'''
    try:
        file = CodeFile.objects.get(id=file_id)
        file_path = os.path.join(BASE_DIR,f'{file.file}')
        os.remove(file_path)
        file.delete()
        return JsonResponse({"message": "File deleted successfully"})
    except CodeFile.DoesNotExist:
        return JsonResponse({"error": "File not found"}, status=404)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

def edit_file(request,file_id):
    '''изменение содержимого файла'''
    file_path =CodeFile.objects.get(id = file_id).file
    full_path = os.path.join(BASE_DIR,f'{file_path}')
    with open(full_path, 'r') as file:
        code_content = file.read()
    context = {'code':code_content,'file_id':file_id}
    return render(request,'edit_file.html',context=context)

@csrf_exempt
def save_file(request):
    """сохранение изменений в файле"""
    if request.method == "POST":
        content = request.POST.get("content")
        file_id = request.POST.get("file_id")
        file = CodeFile.objects.get(id = file_id)
        full_path = os.path.join(BASE_DIR,f'{file.file}')
        try:
            with open(full_path, "w") as file_os:
                file_os.write(content)
            file.status = 'updated'
            file.save()
            return JsonResponse({"message": "File competely save"})
        except Exception as e:
            print(e)
            return JsonResponse({"error": f"File saving error: {str(e)}"}, status=500)
    return JsonResponse({"error": "Uncorrect request"}, status=400)

