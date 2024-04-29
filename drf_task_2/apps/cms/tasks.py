from django.template.loader import get_template
from django.http import HttpResponse
from django.utils.html import escape

import os
from celery import shared_task
from config import settings
from xhtml2pdf import pisa

def create_pdf_from_html(html_content, file_path):
    with open(file_path, 'wb') as pdf_file:
        pisa.CreatePDF(html_content, dest=pdf_file)

#@shared_task()
def process_retrieve_action(user_id):

    from apps.common.models import User 
    from apps.web.serializers import UserReadSerializer

    user = User.objects.get(pk=user_id)
    serializer = UserReadSerializer(instance=user)
    user_data = serializer.data


    template = get_template('userpdf.html')
    html_content = template.render({'user': user_data})


    file_path = os.path.join(settings.BASE_DIR, 'saved_files', f'user_{user_id}.pdf')
    os.makedirs(os.path.dirname(file_path), exist_ok=True)


    create_pdf_from_html(html_content, file_path)

    return file_path