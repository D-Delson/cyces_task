from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from apps.common.models import UserProfile
from decouple import config

@receiver(post_save, sender=UserProfile)
def send_registration_email(sender, instance, created, **kwargs):
    if created:
        subject = 'Welcome to Our Website!'
        message = f'Thankyou for registering with our website {instance.name}'
        sender_email = config('EMAIL_HOST_USER')
        recipient_email = instance.email
        send_mail(subject, message, sender_email, [recipient_email])