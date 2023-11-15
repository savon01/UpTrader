from django.urls import path
from .views import menu_view, vegetables, fruits, computers, laptops

app_name = 'menuapp'

urlpatterns = [
    path('', menu_view, name='menu_view'),
    path('vegetables/', vegetables, name='vegetables'),
    path('fruits/', fruits, name='fruits'),
    path('computers/', computers, name='computers'),
    path('laptops/', laptops, name='laptops'),
]
