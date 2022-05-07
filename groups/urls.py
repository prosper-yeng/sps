from django.urls import path
from rest_framework import routers
from .views import GroupDetails, GroupViewSet, UpdateGroup, UpdateGroupStatus

router = routers.DefaultRouter()
router = routers.DefaultRouter()
router.register('api/group', GroupViewSet, 'group')

urlpatterns = router.urls

# urlpatterns = [
#     path('api/group', GroupView.as_view(), name='group'),
# ]
#
# urlpatterns += router.urls

