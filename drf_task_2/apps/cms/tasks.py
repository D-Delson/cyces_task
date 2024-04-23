from celery import shared_task
from apps.common.models import User  
from apps.web.serializers import UserSerializers

@shared_task
def process_retrieve_action(user_id):
    user = User.objects.get(pk=user_id)
    serialized_user = UserSerializers(user).data
    return serialized_user
    
