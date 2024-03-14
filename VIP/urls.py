from django.urls import path
from .views import VIP, VIPDetails, VIPPrivateClass, VIPEnroll

urlpatterns = [
    path('classes/vip', VIP, name='VIP'),
    path('classes/vip/<str:id>', VIPDetails, name='VIPDetails'),
    path('classes/vip/private/<str:id>', VIPPrivateClass, name='VIPClass'),
    path('classes/vip/enroll/<str:id>', VIPEnroll, name='VIPEnroll'),
]
