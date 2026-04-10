from django.shortcuts import render
from django.core.paginator import Paginator
from django.core.cache import cache
from django.http import JsonResponse
import requests

def index(request):
    # return the main page
    return render(request, 'restaurants/index.html')

def search_by_postcode(request):

    # types of cuisine not consider as restaurants
    exclude_cuisines = ["Deals", "Collect stamps", "Alcohol", "Beauty", "Electronics", "Local Legends", "Pharmacy", 'All Night Alcohol', 'Groceries', "£8 off", "Your favourites", "Meal deal", "Cheeky Tuesday", 'Shops']
    
    restaurants = []
    
    if 'searchPostCode' in request.GET:

        # retrieve the postcode send in the search
        postcode = request.GET['searchPostCode']

        # verify if there are blank spaces in the postcode and remove them 
        if ' ' in postcode:
            postcode = str(postcode).replace(' ', '')

        # check if the list of restaurants is already cached
        cache_restaurants = f'restaurants_{postcode}'
        restaurants = cache.get(cache_restaurants)

        # whether the list of restaurants does not exist
        if restaurants is None:
      
            jet_api_url = f'https://uk.api.just-eat.io/discovery/uk/restaurants/enriched/bypostcode/{postcode}'

            # try to obtain a list of all restaurants available according to the postcode
            try:
                # define the headers to avoid bad requests
                headers = {
                    "User-Agent": (
                        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                        "AppleWebKit/537.36 (KHTML, like Gecko) "
                        "Chrome/123.0.0.0 Safari/537.36"
                    ),
                    "Accept": "application/json",
                }
                
                response = requests.get(jet_api_url, headers=headers)
                
                # the request was unsuccessful
                if response.status_code != 200:
                    print('No restaurants are available in the area')
                    return render(request, 'restaurants/restaurants.html', {'error': 'No restaurants are available in the area'})
                
                # the request was successful
                response_json = response.json()    

                restaurants = []       

                # reads the list of restaurants to obtain only the necessary data
                for restaurant in response_json['restaurants']:

                    # filter the cuisines of the restaurant
                    restaurant_cuisines = [cuisine['name'] for cuisine in restaurant['cuisines'] if cuisine['name'] not in exclude_cuisines]

                    if restaurant_cuisines != []:
                        
                        restaurants.append({
                            'uniqueName': restaurant['uniqueName'],
                            'name': restaurant['name'],
                            'address': {
                                'firstLine': str(restaurant['address']['firstLine']).title(),
                                'city': str(restaurant['address']['city']).title()
                            }
                            ,
                            'rating': restaurant['rating'],
                            'cuisines': restaurant_cuisines,
                            'logoUrl': restaurant['logoUrl']
                        })
                
                # Cache the list of restaurants
                cache.set(cache_restaurants, restaurants, timeout=300)
            
            # improve the error handling
            except requests.exceptions.RequestException as error:
                return render(request, 'restaurants/restaurants.html', {'error': f'Error in the request: {error}'})
            except requests.exceptions.JSONDecodeError as error_json:
                return f'The response contains invalid JSON. {error_json}'
            except requests.exceptions.HTTPError as bad_request:
                return f'A bad request was made. {bad_request}'

        pagination = Paginator(restaurants, 10)
        page_number = request.GET.get('page')
        page_object = pagination.get_page(page_number)
        
        return render(request, 'restaurants/pagination.html', {
            'page_object': page_object,
            'postcode': postcode
        })
