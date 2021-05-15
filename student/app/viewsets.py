from rest_framework import viewsets
from rest_framework import permissions

from .serializers import StudentSerializer
from .models import Student

class StudentViewset(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAuthenticated]