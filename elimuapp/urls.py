
from django.contrib import admin
from django.urls import path
from elimuapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('coursedetails/', views.coursedeatils, name='coursedetails'),
    path('courses/', views.courses, name='courses'),
    path('events/', views.events, name='events'),
    path('pricing/', views.pricing, name='pricing'),
    path('starter/', views.starter, name='starter'),
    path('trainers/', views.home, name='home'),
]
