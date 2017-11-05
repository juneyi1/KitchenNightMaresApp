from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import render, get_object_or_404

from .models import Restaurant 
# Create your views here.
def index(request):
    restaurant_list = Restaurant.objects.order_by('name')#[:5]
    #template = loader.get_template('restaurants/index.html')
    context = {'restaurant_list': restaurant_list}
    return render(request, 'restaurants/index.html', context)
#    return HttpResponse(template.render(context, request))

def detail(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
#    try:
#        restaurant = Restaurant.objects.get(pk=restaurant_id)
#    except Restaurant.DoesNotExist:
#        raise Http404("Restaurant does not exist")
    return render(request, 'restaurants/detail.html', {'restaurant': restaurant})
