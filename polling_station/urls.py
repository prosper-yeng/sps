from django.urls import path
from rest_framework import routers
from .views import PollingStationViewset

router = routers.DefaultRouter()
router.register('api/polling_station', PollingStationViewset, 'polling_station')
urlpatterns = router.urls


