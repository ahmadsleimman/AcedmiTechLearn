from django.urls import path
from .views import Online, OnlineDetails, OnlineEnroll

urlpatterns = [
    path('classes/online', Online, name='Online'),
    path('classes/online/<str:id>', OnlineDetails, name='OnlineDetails'),
    path('classes/online/enroll/<str:id>', OnlineEnroll, name='OnlineEnroll'),
]
