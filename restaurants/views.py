from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import render, get_object_or_404

from .models import Restaurant
from .forms import SearchForm


def index(request):
    restaurant_list = Restaurant.objects.order_by('name')

    context = {
        'restaurant_list': restaurant_list,
        # 'all_neighborhoods': Restaurant.get_all_neighborhoods(),
        # 'all_categories': Restaurant.get_all_categories(),
        # 'all_prices_ranges': Restaurant.get_all_prices_ranges(),

        'form': SearchForm()  # Empty search form
    }
    return render(request, 'restaurants/index.html', context)


def detail(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
    return render(request, 'restaurants/detail.html', {'restaurant': restaurant})


def search(request):
    form = SearchForm(request.GET)

    if not form.is_valid():
        # Error!
        return HttpResponse(status=500)

    neighborhood = form.data['neighborhood']
    price_range = form.data['price_range']
    category = form.data['category']

    possible_restaurants = Restaurant.get_from_search(
                                neighborhood,
                                price_range,
                                category
                            )

    return render(request,
                  'restaurants/search_results.html',
                  {'restaurants': possible_restaurants}
                  )
