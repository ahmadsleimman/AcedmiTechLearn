from django.urls import path
from .views import Classes, ClassDetails, ClassEnroll

urlpatterns = [
    path('classes', Classes, name='Classes'),
    path('classes/<str:id>', ClassDetails, name='ClassDetails'),
    path('classes/enroll/<str:id>', ClassEnroll, name='ClassEnroll'),
]
