from django.urls import path
from .views import *


urlpatterns = [
    path('admin/register/', AdminAPIView.as_view(), name='admin_register'),
    path('jobseeker/register/', JobSeekerAPIView.as_view(), name='admin_register'),
    path('job/register/', JobAPIView.as_view(), name='admin_register'),
    path('logout/', LogoutView.as_view(), name='logout'),
]