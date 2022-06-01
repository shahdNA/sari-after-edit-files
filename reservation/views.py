from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView, CreateView, DetailView, ListView

from .models import Restaurant, City
from .forms import RestaurantForm


def list_all_restaurants(request):
    restaurants = Restaurant.objects.all()

    return render(
        request,
        'reservation/list_restaurants.html',
        context={
            'restaurants': restaurants,
        }
    )


def restaurant_details(request, pk):
    restaurant = get_object_or_404(Restaurant, pk=pk)
    return render(request, 'reservation/restaurant_details.html', context={'restaurant': restaurant, })


def search_restaurants(request, search_query=''):
    restaurants = Restaurant.objects.filter(name__contains=search_query)

    return render(
        request,
        'reservation/list_restaurants.html',
        context={
            'restaurants': restaurants,
        }
    )


def city_restaurants(request, city_pk):
    restaurants = Restaurant.objects.filter(city__pk=city_pk)

    return render(
        request,
        'reservation/city.html',
        context={
            'restaurants': restaurants,
        }
    )


def country_restaurants(request, country_pk):
    cities = City.objects.filter(country__pk=country_pk)

    return render(
        request,
        'reservation/country.html',
        context={
            'cities': cities,
        }
    )


def restaurant_edit(request, pk):
    restaurant = get_object_or_404(Restaurant, pk=pk)
    form = RestaurantForm(request.POST or None, instance=restaurant)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, '{}restaurant was saved'.format(restaurant))
            return redirect('list-restaurants')
        else:
            print(form.errors)

    return render(
        request,
        'reservation/restaurant_edit.html',
        context={
            'restaurant': restaurant,
            'form': form,

        }
    )


class BaseRestaurantManipulateView(SuccessMessageMixin, LoginRequiredMixin):
    template_name = 'reservation/restaurant_edit.html'
    model = Restaurant
    form_class = RestaurantForm
    success_url = reverse_lazy('list-restaurant')
    success_message = 'The Data Was Saved'


class RestaurantUpdateView(BaseRestaurantManipulateView, UpdateView):
    pass


class RestaurantCreateView(BaseRestaurantManipulateView, CreateView):
    pass


class RestaurantDetailView(DetailView):
    template_name = 'reservation/restaurant_details.html'
    model = Restaurant
    success_url = reverse_lazy('list-restaurant')


class RestaurantListView(ListView):
    template_name = 'reservation/list_restaurants.html'
    model = Restaurant
    context_object_name = 'restaurants'


