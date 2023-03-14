from django.urls import path

from calculator.views import calculate_savings

urlpatterns = [
    path('', calculate_savings, name='calculate'),
]