from django.contrib import admin
from users.models import User, Payment


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "email", "avatar", "phone", "user_city")


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "paid_at",
        "payment_type",
        "course",
        "lesson",
        "payment_sum",
    )
