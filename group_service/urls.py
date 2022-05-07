from django.urls import path
from rest_framework import routers
from .views import GroupServiceViewSet

router = routers.DefaultRouter()
router.register('api/group_service', GroupServiceViewSet, 'group_service')

urlpatterns = router.urls


