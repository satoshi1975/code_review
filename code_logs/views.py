from django.http import JsonResponse
from django.shortcuts import render
from main.models import CustomUser
from upload.models import CodeFile
from code_review.models import CheckLog

def logs_page(request,user_id):
    # user = CustomUser.objects.get(id = user_id)
    list_of_files = CodeFile.objects.filter(user_id = user_id)
    context = {"list_of_files":list_of_files}
    return render(request,'logs_page.html',context)

def get_logs(request,file_id):
    print("COMPLETE")
    
    if CheckLog.objects.filter(file_id=file_id).exists():
        logs = CheckLog.objects.get(file_id=file_id)
        if logs.mailed == False:
            return JsonResponse({'logs':logs.details + ('(Not sent)')})
        else:
            return JsonResponse({'logs':logs.details + ('Sent')})
    else:   
        return JsonResponse({'logs':'None'}) 
    
    
    
