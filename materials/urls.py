from tkinter.font import names

from django.urls import path
from rest_framework.routers import SimpleRouter

from materials.apps import MaterialsConfig
from materials.models import Course
from materials.views import (
    LessonCreateApiView,
    LessonDestroyApiView,
    LessonListApiView,
    LessonRetrieveApiView,
    LessonUpdateApiView,
    CourseViewSet, SubscriptionCreateAPIView, SubscriptionDestroyAPIView, SubscriptionListApiView,
)

app_name = MaterialsConfig.name

router = SimpleRouter()
router.register("", CourseViewSet)

urlpatterns = [
    path("classes/", LessonListApiView.as_view(), name="classes_list"),
    path("classes/<int:pk>/", LessonRetrieveApiView.as_view(), name="classes_retrieve"),
    path("classes/create/", LessonCreateApiView.as_view(), name="classes_create"),
    path("classes/<int:pk>/delete/", LessonDestroyApiView.as_view(), name="classes_delete",),
    path("classes/<int:pk>/update/", LessonUpdateApiView.as_view(), name="classes_update"),
    path('<int:pk>/subscription/create/', SubscriptionCreateAPIView.as_view(), name='subscription_create'),
    path('subscription/', SubscriptionListApiView.as_view(), name='subscriptions_list'),
    path('subscription/<int:pk>/delete/', SubscriptionDestroyAPIView.as_view(), name='subscription_delete'),
]

urlpatterns += router.urls
