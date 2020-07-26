from django.urls import path
from .views import rest, forecast

urlpatterns = [
    path('', rest, name='rest'),
    path('forecast/',forecast, name='forecast'),
]
