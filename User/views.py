from django.shortcuts import render, HttpResponse

def index(request):
    return render (request, 'Index.html')


def feedback(request):
    return render (request, 'Feedback.html')


def about(request):
    return render (request, 'About.html')


