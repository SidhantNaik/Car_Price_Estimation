from django.shortcuts import render, redirect
from User.models import Feedback
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages



def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signin')
    else:
        form = UserCreationForm()
    return render(request, 'Signup.html', {'form': form})



def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'Signin.html', {'form': form})


def logoutUser(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect("/login")


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
        messages.success(request,"Your Feedback is submitted succefully !")

    return render (request, 'Feedback.html')


def about(request):
    return render (request, 'About.html')
