from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory
from .viewsets import StudentViewset
class Testcrud(APITestCase):

    def test_create(self):

    	factory = APIRequestFactory()
    	view = StudentViewset.as_view({'post': 'create'})
    	request = factory.post('/api/student',{
            "id": 2,
            "name": "Name 2",
            "email": "name2@email.com",
            "mobile": 1234567891
        })
    	response = view(request)
    	print(response.status_code)
    	self.assertEqual(response.status_code , 201)