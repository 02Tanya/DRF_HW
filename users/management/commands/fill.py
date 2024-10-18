from django.core.management import BaseCommand
from users.models import User, Payment


class Command(BaseCommand):

    def handle(self, *args, **options):
        user_list = [
            {"email": "tr3520@bk.ru", "phone": "89434457658", "user_city": "Рейкъявик"},
            {"email": "mail5600@bk.ru", "phone": "89356734993", "user_city": "Сидней"},
            {
                "email": "ana.stasova@yandex.ru",
                "phone": "89356755993",
                "user_city": "Чикаго",
            },
        ]

        users_for_create = []
        for user_item in user_list:
            users_for_create.append(User(**user_item))
        User.objects.bulk_create(users_for_create)
        #
        # payment_list = [
        #     {"user": 1, "course": 3, "payment_sum": 10000, "payment_type": "Наличные"},
        #     {"user": 2, "course": 3, "payment_sum": 12000, "payment_type": "Перевод на счет"},
        #     {"user": 3, "lesson": 2, "payment_sum": 5000, "payment_type": "Наличные"},
        #     {"user": 2, "course": 4, "payment_sum": 20000, "payment_type": "Перевод на счет"},
        #     {"user": 1, "lesson": 4, "payment_sum": 3000, "payment_type": "Наличные"}
        # ]
        #
        # payments_for_create = []
        # for payment_item in payment_list:
        #     payments_for_create.append(
        #         Payment(**payment_item)
        #     )
        # Payment.objects.bulk_create(payments_for_create)
