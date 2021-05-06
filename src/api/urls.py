from rest_framework import routers
from .app import CourseViewSet

router = routers.DefaultRouter()
router.register("api/courses", CourseViewSet, "courses")

urlpatterns = router.urls
