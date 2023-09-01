from django.shortcuts import render, HttpResponse, redirect
def index(request):
    return render(request, "survey.html")

def survey_submit(request):
    print(request.POST)
    request.session['data'] = request.POST
    print(request.session['data'])
    return redirect("/result")

def result(request):
    print(request.session['data'])
    return render(request, "result.html")