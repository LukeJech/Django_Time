from django.urls import path     
from . import views
urlpatterns = [
    path('', views.toppings),
    path('meats', views.meats),
    path('meats/<str:name>', views.meat_choice),
]
