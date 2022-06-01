"""sari URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from reservation.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('list/', list_all_restaurants, name='list-restaurants', ),
    # path('base/', list_all_restaurants, name='base', ),
    path('city/<int:city_pk>/', city_restaurants, name='city_restaurants', ),
    path('country/<int:country_pk>/', country_restaurants, name='country_restaurants', ),
    path('restaurants_search/', search_restaurants, name='restaurants-search', ),
    path('restaurants_search/<str:search_query>/', search_restaurants, name='restaurants-search-with-query', ),
    # path('details/<int:pk>/', restaurant_details, name='restaurant-details', ),
    # path('edit/<int:pk>/', restaurant_edit, name='restaurant-edit', ),
    path('edit/<int:pk>/', RestaurantUpdateView.as_view(), name='restaurant-edit', ),
    path('create/', RestaurantCreateView.as_view(), name='restaurant-create', ),
    path('detail/<int:pk>/', RestaurantDetailView.as_view(), name='restaurant-details', ),
    path('list/', RestaurantListView.as_view(), name='list-restaurants', ),

]
