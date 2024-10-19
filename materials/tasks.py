import datetime
from celery import shared_task
from config.settings import EMAIL_HOST_USER, TIME_ZONE
from users.models import User
from django.core.mail import send_mail
from materials.models import Subscription


@shared_task
def send_email_about_course_updates(course_pk):
    '''Отправляет пользователю письмо об обновлении курса, на который у него есть подписка.'''
    subscriptions = Subscription.objects.filter(course=course_pk)
    for subscription in subscriptions:
        user = subscription.user
        emails = [user.email]
        course = subscription.course
        send_mail(
            subject="Обновление курса",
            message=f"Добрый день! Курс {course.name} обновлен",
            from_email=EMAIL_HOST_USER,
            recipient_list=emails
        )


@shared_task
def blocks_the_user():
    '''Блокирует пользователя, который не проявлял активности.'''
    now = datetime.datetime.now()
    users = User.objects.filter(is_active=True, is_superuser=False,  last_login__isnull=False)

    for user in users:
        print("start!")
        if user.last_login:
            if user.last_login.timestamp() < (now - datetime.timedelta(days=30)).timestamp():
                user.is_active = False
                user.save()
