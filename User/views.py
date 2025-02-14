from django.shortcuts import render, HttpResponse
from User.models import Feedback

def index(request):
    return render (request, 'Index.html')


def feedback(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        description = request.POST['description']

        feedback = Feedback(name=name, email=email, phone=phone, description=description)
        feedback.save()
    return render (request, 'Feedback.html')


def about(request):
    return render (request, 'About.html')


