from django.shortcuts import HttpResponse, redirect # add redirect to import statement
from django.http import JsonResponse

# Create your views here.
from django.shortcuts import render, HttpResponse
def cheeses(request):
    return HttpResponse("Motzzz and a ton please!")

def vegan(request):
    return redirect("toppings/meats")