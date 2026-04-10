from django.urls import path
from restaurants.views import index, search_by_postcode

urlpatterns = [
    path('', index, name='index'),
    path('pagination/', search_by_postcode, name='pagination'),
]