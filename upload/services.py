
from .models import CodeFile
from code_review.models import CheckLog
from code_check.settings import BASE_DIR
import os


def upload_file(request):
    '''обработка загруженного файла'''
    uploaded_file = request.FILES.get('file')
    if uploaded_file:

        code_file = CodeFile.objects.create(
            user=request.user, file=uploaded_file, name=uploaded_file.name)

        user_id = request.user.id
        file_path = os.path.join(
            BASE_DIR, 'user_code', f'{user_id}', f'{uploaded_file.name}')
        
        with open(file_path, 'wb') as destination:
            for chunk in uploaded_file.chunks():
                destination.write(chunk)
        CheckLog.objects.create(file=code_file)
        return {'id': code_file.id, 'name': code_file.name}
    else:
        return False
