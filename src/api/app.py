from api.models import Course
from rest_framework import viewsets, permissions
from .serializers import CourseSerializer

# Api Viewsets
class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CourseSerializer
