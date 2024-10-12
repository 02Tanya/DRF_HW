from django.db import models
from rest_framework.viewsets import ModelViewSet


class Course(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Название курса",
        help_text="Введите название курса",
    )
    description = models.TextField(
        verbose_name="Описание курса",
        help_text="Введите описание курса"
    )
    preview = models.ImageField(
        upload_to='materials/preview',
        blank=True,
        null=True,
        verbose_name="Превью",
        help_text="Загрузите превью курса",
    )

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
        verbose_name="Описание урока",
        help_text="Введите описание урока"
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

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
        ordering = ["name", "course"]

    def __str__(self):
        return self.name
