from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse("This is Index page.")


def feedback(request):
    return HttpResponse("This is Feedback page.")


def about(request):
    return HttpResponse("This is About page.")


