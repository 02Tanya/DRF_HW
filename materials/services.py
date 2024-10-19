from config.settings import STRIPE_SECRET_KEY
from django.conf import settings
from django.core.mail import send_mail
import stripe
from materials.models import Subscription

stripe.api_key = STRIPE_SECRET_KEY


def create_link_for_payment(payment_sum):
    '''Создает продукт, цену и ссылку на оплату в страйпе'''
    product = stripe.Product.create(name='course')

    product_price = stripe.Price.create(
        unit_amount=payment_sum,
        currency="usd",
        product=product.get("id"),
    )

    payment_link = stripe.PaymentLink.create(
        line_items=[{"price": product_price.get("id"), "quantity": 1}],
    )

    return payment_link.get("url")


# def send_email_about_updating(course_pk):
#     '''Отправляет пользователю письмо об обновлении курса, на который у него есть подписка.'''
#     subscriptions = Subscription.objects.filter(course=course_pk)
#     for subscription in subscriptions:
#         user = subscription.user
#         emails = [user.email]
#         course = subscription.course
#
#         send_mail(
#             subject="Обновление курса",
#             message=f"Добрый день! Курс {course.name} обновлен",
#             from_email=settings.EMAIL_HOST_USER,
#             recipient_list=emails
#         )