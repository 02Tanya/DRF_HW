from django.urls import reverse
from rest_framework import status

from rest_framework.test import APITestCase, APIClient

from materials.models import Lesson, Course, Subscription
from users.models import User


class LessonAPITestCase(APITestCase):

    def setUp(self):
        # self.client = APIClient()
        self.user = User.objects.create(email='test22@test.ru')
        self.client.force_authenticate(user=self.user)

        self.course = Course.objects.create(
            name='Лесные заклятья',
            description='Самое лучшее колдовство в лесу',
        )
        self.lesson = Lesson.objects.create(
            name='Лесные приметы',
            description='Самые действенные лесные приметы',
            course=self.course,
            url="https://youtube.com/forestdreams/",
            author=self.user
        )


    def test_lesson_retrieve(self):
        '''Тестирование просмотра данных об уроке.'''
        url = reverse("materials:classes_retrieve", args=(self.lesson.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), self.lesson.name)


    def test_lesson_create(self):
        '''Тестирование создания урока.'''
        url = reverse("materials:classes_create")
        data = {
            "name": "Колдовские зелья",
            "description": "Основы изготовления зелий",
            "url": "https://youtube.com/forestjuice/"
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Lesson.objects.all().count(), 2)


    def test_lesson_update(self):
        '''Тестирование обновления данных урока.'''
        url = reverse("materials:classes_update", args=(self.lesson.pk,))
        data = {
            "name": "Колдовские зелья и варево"
        }
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), "Колдовские зелья и варево")


    def test_lesson_delete(self):
        '''Тестирование удаления урока.'''
        url = reverse("materials:classes_delete", args=(self.lesson.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Lesson.objects.all().count(), 0)


    def test_lesson_list(self):
        '''Тестирование просмотра списка уроков.'''
        url = reverse("materials:classes_list")
        response = self.client.get(url)
        data = response.json()
        result = {
                'count': 1,
                'next': None,
                'previous': None,
                'results': [
                    {
                        'id': self.lesson.pk,
                        'name': self.lesson.name,
                        'description': self.lesson.description,
                        'image': None,
                        'url': self.lesson.url,
                        'course': self.course.pk,
                        'author': self.user.pk
                    }
                ]
            }
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)



class SubscriptionAPITestCase(APITestCase):

    def setUp(self):
        # self.client = APIClient()
        self.user = User.objects.create(email='test22@test.ru')
        self.client.force_authenticate(user=self.user)

        self.course = Course.objects.create(
            name='Лесные заклятья',
            description='Самое лучшее колдовство в лесу',
        )
        self.subscription = Subscription.objects.create(
            user=self.user,
            course=self.course,
        )


    def test_subscription_create(self):
        '''Тестирование создания подписки.'''
        data = {
            "user": self.user.pk,
            "course": self.course.pk,
        }
        response = self.client.post(f'/materials/{self.course.pk}/subscription/create/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Subscription.objects.all().count(), 2)


    def test_subscription_delete(self):
        '''Тестирование удаления подписки.'''
        data = {
            "user": self.user.pk,
            "course": self.course.pk,
        }
        response = self.client.delete(f'/course/subscription/{self.subscription.pk}/delete/', data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
