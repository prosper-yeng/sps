from django.urls import path
from rest_framework import routers
from .views import  LoginView, UserView, LogoutView, UserViewSet

router = routers.DefaultRouter()
router.register('api/user', UserViewSet, 'user')
#router.register('api/login', LoginView.as_view(), 'login')
#router.register('api/patient', PatientViewSet, 'patient')
#router.register('api/staff', StaffViewSet, 'staff')


urlpatterns = [
    path ( 'api/user', UserView.as_view (), name='user'),
    path('api/login', LoginView.as_view(), name='login'),
    path('api/logout', LogoutView.as_view(), name='logout'),
    # path('api/patient', PatientView.as_view(), name='patient'),
]
urlpatterns += router.urls


