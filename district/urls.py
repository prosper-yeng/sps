from django.urls import path
from rest_framework import routers
from .views import DistrictViewset

router = routers.DefaultRouter()
router.register('api/district', DistrictViewset, 'district')
urlpatterns = router.urls


