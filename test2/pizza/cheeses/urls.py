from django.urls import path     
from . import views
urlpatterns = [
    path('', views.cheeses),
    path('vegan', views.vegan),
]
