from api.models import Course
from rest_framework import generics
from .serializers import CourseSerializer


# Api Views
class CourseList(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
