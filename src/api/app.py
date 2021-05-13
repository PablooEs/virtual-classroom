from api.models import Course
from rest_framework import viewsets, permissions
from .serializers import CourseSerializer

# Api Viewsets


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
