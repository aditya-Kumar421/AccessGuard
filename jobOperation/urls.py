from django.urls import path
from .views import PersonalDataListAPIView, JobDataView, AdminContentView

urlpatterns = [
    path('personaldata/', PersonalDataListAPIView.as_view(), name='personaldata-list'),
    path('jobdata/', JobDataView.as_view(), name='jobgiver-list-create'),
    path('admincontent/', AdminContentView.as_view(), name='admin-content-list-create'),
    
]
