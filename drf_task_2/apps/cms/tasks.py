import os
import json
from celery import shared_task
from config import settings
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

#@shared_task()
def process_retrieve_action(user_id):

    from apps.common.models import User 
    from apps.web.serializers import UserReadSerializer
    user = User.objects.get(pk=user_id)
    serialized_user_data = UserReadSerializer(user).data
    
    file_path = os.path.join(settings.BASE_DIR, 'saved_files', f'user_{user_id}.pdf')
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    c = canvas.Canvas(file_path, pagesize=letter)

    json_data = json.dumps(serialized_user_data, indent=4)  # Convert JSON data to formatted string
    lines = json_data.split('\n')
    y_offset = 730  # Initial y-coordinate
    for line in lines:
        c.drawString(100, y_offset, line)
        y_offset -= 10
    c.showPage()
    c.save()

    return file_path

    
    # with open(file_path, 'w') as file:
    #     json.dump(serialized_user_data, file)
    #return file_path