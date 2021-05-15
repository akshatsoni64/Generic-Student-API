from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory
from rest_framework import status
from django.shortcuts import reverse
from .models import Student
from .serializers import StudentSerializer
import json


class TestNoteApi(APITestCase):
    url_one = reverse('student-list')
    # url_two = reverse('student-detail')

    def setUp(self):
        self.factory = APIRequestFactory()
        self.user = User.objects.create(username="root", password="root123")
        self.student = Student.objects.create(name="Name 0", email="name0@email.com", age=20)
        self.client.force_authenticate(user=self.user)
        print("\nStudent Data:", StudentSerializer(Student.objects.all(), many=True).data)

    def test_creation(self):
        response = self.client.post(self.url_one, {
            'name': 'Name 1',
            'email': 'new1@email.com',
            'age': 21
        })
        print('CREATE:',response.status_code)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list(self):
        response = self.client.get(self.url_one)
        print('LIST:',response.status_code)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update(self):
        get_response = self.client.get(self.url_one)
        response = self.client.put(
            reverse(
                'student-detail',
                kwargs={
                    "pk": get_response.data[0]['id']
                }
            ),
            {
                "name": "New Name",
                "email": "new_email@email.com",
                "age": 20
            }
        )
        print("UPDATE", response.status_code, "DATA:", response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_destroy(self):
        response = self.client.delete(reverse('student-detail', kwargs={"pk": 3}))
        print("DESTROY", response.status_code)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)