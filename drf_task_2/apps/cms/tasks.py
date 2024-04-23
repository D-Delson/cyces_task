import os
import json
from celery import shared_task
from config import settings


@shared_task
def process_retrieve_action(user_id):

    from apps.common.models import User 
    from apps.web.serializers import UserSerializers
    print('I am working')
    user = User.objects.get(pk=user_id)
    serialized_user_data = UserSerializers(user).data
    
    file_path = os.path.join(settings.BASE_DIR, 'saved_files', f'user_{user_id}.json')
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'w') as file:
        json.dump(serialized_user_data, file)
    return file_path