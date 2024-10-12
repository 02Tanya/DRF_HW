from django.contrib.auth.models import AbstractUser
from django.db import models

from materials.models import Course, Lesson


class User(AbstractUser):
    username = None
    email = models.EmailField(
        unique=True,
        verbose_name="Email",
        help_text="Введите Ваш email"
    )
    avatar = models.ImageField(
        upload_to='users/avatars',
        blank=True,
        null=True,
        verbose_name="Фото",
        help_text="Загрузите ваше фото",
    )
    phone = models.CharField(
        max_length=35,
        blank=True,
        null=True,
        verbose_name='Номер телефона',
        help_text='Введите ваш номер',
    )
    user_city = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name='Название города',
        help_text='Введите название города',
    )
    # token = models.CharField(
    #     max_length=100,
    #     blank=True,
    #     null=True,
    #     verbose_name='Token'
    # )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email



class Payment(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
        help_text="Введите пользователя",
        related_name="paid_users",
    )
    paid_at = models.DateField(
        blank=True,
        null=True,
        verbose_name="Дата оплаты",
        help_text="Введите дату оплаты",
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.SET_NULL,
        verbose_name="Название курса",
        help_text="Введите название курса",
        null=True,
        blank=True,
        related_name="paid_courses",
    )
    lesson = models.ForeignKey(
        Lesson,
        on_delete=models.SET_NULL,
        verbose_name="Название урока",
        help_text="Введите название урока",
        null=True,
        blank=True,
        related_name="paid_lessons",
    )
    payment_sum = models.IntegerField(
        verbose_name="Сумма оплаты", help_text="Введите сумму оплаты"
    )
    payment_type = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name='Способ оплаты',
        help_text='Укажите способ оплаты',
    )
    # cash = 'Наличные'
    # invoice = 'Перевод на счет'


    class Meta:
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежи'

    def __str__(self):
        return self.payment_type
