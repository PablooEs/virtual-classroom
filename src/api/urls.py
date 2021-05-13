from django.urls import path
from .views.CourseView import CourseList, CourseDelete
urlpatterns = [
    path('courses', CourseList.as_view()),
    path('courses/<int:pk>', CourseDelete.as_view())
]
