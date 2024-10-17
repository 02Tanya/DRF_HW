from django.contrib import admin
from materials.models import Course, Lesson


@admin.register(Course)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description", "preview", "author")

@admin.register(Lesson)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description", "image", "course", "url", "author")
