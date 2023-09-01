from django.shortcuts import render, HttpResponse, redirect, render
from django.http import JsonResponse
from time import gmtime, strftime

def root(request):
    context = {
        "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
    }
    return render(request, 'my_time.html', context)