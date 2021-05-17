from django.urls import path

from weather.api.rest.views import get_weather_by_city

urlpatterns = [
    path('city/<str:city_name>', get_weather_by_city)
]
