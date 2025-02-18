from django.contrib import admin
from django.urls import path
from User import views

urlpatterns = [
    path('', views.index, name='index'), #Dispaly index page.
    path('feedback', views.feedback, name='feedback'), #Dispaly feedback page.
    path('about', views.about, name='about'), #Dispaly about page.
    path('signin', views.signin, name='signin'), #Dispaly signin page.
    path('signup', views.signup, name='signup'), #Dispaly signup page.
]