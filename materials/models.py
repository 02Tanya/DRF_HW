from django.db import models
from rest_framework.viewsets import ModelViewSet
from django.conf import settings


class Course(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Название курса",
        help_text="Введите название курса",
    )
    description = models.TextField(
        verbose_name="Описание курса", help_text="Введите описание курса"
    )
    preview = models.ImageField(
        upload_to="materials/preview",
        blank=True,
        null=True,
        verbose_name="Превью",
        help_text="Загрузите превью курса",
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Автор",
        help_text="Укажите автора",
    )
    # subscriptions=models.ManyToManyField(
    #     settings.AUTH_USER_MODEL,
    #     null=True,
    #     blank=True,
    #     verbose_name='Подписки',
    #     help_text='Укажите подписки',
    #     related_name="user_subscriptions"
    # )

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Lesson(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Название урока",
        help_text="Введите название урока",
    )
    description = models.TextField(
        verbose_name="Описание урока", help_text="Введите описание урока"
    )
    image = models.ImageField(
        upload_to="product/photo",
        blank=True,
        null=True,
        verbose_name="Превью",
        help_text="Загрузите фото продукта",
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        verbose_name="Название курса",
        help_text="Введите название курса",
        null=True,
        blank=True,
        related_name="courses",
    )
    url = models.URLField(
        max_length=500,
        null=True,
        blank=True,
        verbose_name="Ссылка нв урок",
        help_text="Укажите ссылку на урок",
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Автор",
        help_text="Укажите автора",
    )

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
        ordering = ["name", "course"]

    def __str__(self):
        return self.name


class Subscription(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="subscriptions",
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="subscriptions"
    )

    def __str__(self):
        return f"{self.pk}: user - {self.user} course - {self.course}"

    class Meta:
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"
