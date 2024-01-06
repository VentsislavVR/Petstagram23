# Best option gor sending emails
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver


from core.email_utils import send_email_with_template

UserModel = get_user_model()


def send_successful_registration_email(user):
    context = {
        'user': user
    }
    send_email_with_template(
        subject='Successful registration',
        template_name='emails/email-greeting.html',
        context=context,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[user.email],
    )



@receiver(post_save, sender=UserModel)
def user_created(instance, created, **kwargs):
    if created:
        send_successful_registration_email(instance)
