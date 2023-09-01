from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse
def toppings(request):
    return HttpResponse("Gimme pepporoni plz")

def meats(request):
    return HttpResponse("Gimme bacon, sausage and the whole meat pie plz")

def meat_choice(request, name):
    return HttpResponse(f'I want to add {name} to my pizza')