from django.urls import path
from .views import Offline, OfflineDetails, OfflineEnroll

urlpatterns = [
    path('classes/offline', Offline, name='Offline'),
    path('classes/offline/<str:id>', OfflineDetails, name='OfflineDetails'),
    path('classes/offline/enroll/<str:id>', OfflineEnroll, name='OfflineEnroll'),
]
