from rest_framework.routers import DefaultRouter
from app import viewsets

router = DefaultRouter()
router.register(r'student', viewsets.StudentViewset, basename="student")