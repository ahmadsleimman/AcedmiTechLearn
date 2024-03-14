from django.urls import path
from .views import Online, OnlineDetails, OnlineEnroll, OnlineOfferDetails, OnlineOfferEnroll

urlpatterns = [
    path('classes/online', Online, name='Online'),
    path('classes/online/<str:id>', OnlineDetails, name='OnlineDetails'),
    path('classes/online/enroll/<str:id>', OnlineEnroll, name='OnlineEnroll'),
    path('classes/online/offer/<str:id>', OnlineOfferDetails, name='OnlineOffer'),
    path('classes/online/offer/<str:id>/enroll', OnlineOfferEnroll, name='OnlineOfferEnroll'),
]
