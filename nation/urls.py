from django.urls import path
from rest_framework import routers
from .views import DistrictViewset

router = routers.DefaultRouter()
router.register('api/nation', DistrictViewset, 'nation')
urlpatterns = router.urls


