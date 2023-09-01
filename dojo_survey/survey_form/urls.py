from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('survey_submit' , views.survey_submit),
    path('result', views.result)
]
