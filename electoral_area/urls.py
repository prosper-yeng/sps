from django.urls import path
from rest_framework import routers
from .views import ElectoralAreaViewset

router = routers.DefaultRouter()
router.register('api/electoral_area', ElectoralAreaViewset, 'electoral_area')
urlpatterns = router.urls


