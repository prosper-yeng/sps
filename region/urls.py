from django.urls import path
from rest_framework import routers
from .views import RegionViewset

router = routers.DefaultRouter()
router.register('api/region', RegionViewset, 'region')
urlpatterns = router.urls


