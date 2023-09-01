from django.shortcuts import render, HttpResponse
def index(request):
    return HttpResponse("catch dem all")

def chicken(request):
    return HttpResponse('Give me more chikcennnn')