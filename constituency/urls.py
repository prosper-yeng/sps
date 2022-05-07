from django.urls import path
from rest_framework import routers
from .views import ConstituencyViewset

router = routers.DefaultRouter()
router.register('api/constituency', ConstituencyViewset, 'constituency')
urlpatterns = router.urls


