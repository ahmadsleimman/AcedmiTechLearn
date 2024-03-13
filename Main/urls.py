from django.urls import path
from .views import Home, About, ContactUs, Service, NotFound
urlpatterns = [
    path('', Home, name='Home'),

    # path('login', loginUser, name='Login'),

    # path('register', registerUser, name='Register'),

    # path('logout', logout, name='Logout'),

    path('about', About, name='About'),

    path('service', Service, name='Service'),

    path('contact-us', ContactUs, name='Contact'),

    # path('myclasses', MyClasses, name='MyClasses'),

    path('404', NotFound, name='NotFound'),
]
