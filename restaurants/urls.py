from django.urls import path
from restaurants.views import index, search_restaurant_by_postcode, search_by_postcode

urlpatterns = [
    path('', index, name='index'),
    path('search/', search_restaurant_by_postcode, name='search'),
    path('pagination/', search_by_postcode, name='pagination'),
]