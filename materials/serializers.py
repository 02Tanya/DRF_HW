from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from materials.models import Lesson, Course, Subscription
from materials.validators import LinkValidator


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"
        validators = [LinkValidator(field="url")]


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"
        # validators = [
        #     LinkValidator(field='description')
        # ]


class CourseDetailSerializer(ModelSerializer):
    lessons_in_course = SerializerMethodField()
    lesson = LessonSerializer(many=True, read_only=True, source="courses")

    def get_lessons_in_course(self, course):
        return Lesson.objects.filter(course=course).count()

    class Meta:
        model = Course
        fields = ("name", "description", "lessons_in_course", "lesson")


class SubscriptionSerializer(ModelSerializer):

    class Meta:
        model = Subscription
        fields = '__all__'