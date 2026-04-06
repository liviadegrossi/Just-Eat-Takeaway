from django.urls import path
from restaurants.views import index

urlpatterns = [
    path('', index, name='index')
]