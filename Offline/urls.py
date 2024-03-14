from django.urls import path
from .views import Offline, OfflineDetails, OfflineEnroll, OfflineOfferDetails, OfflineOfferEnroll

urlpatterns = [
    path('classes/offline', Offline, name='Offline'),
    path('classes/offline/<str:id>', OfflineDetails, name='OfflineDetails'),
    path('classes/offline/enroll/<str:id>', OfflineEnroll, name='OfflineEnroll'),
    path('classes/offline/offer/<str:id>', OfflineOfferDetails, name='OfflineOffer'),
    path('classes/offline/offer/<str:id>/enroll', OfflineOfferEnroll, name='OfflineOfferEnroll'),
]
