"""HotelWebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from hotelsite.views import mainpage, aboutwhatthisis, contactus, reviews, booking, topic_detail, loginpage, register, logoutuser

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mainpage, name = "mainpage"),
    path('aboutwhateverthisis', aboutwhatthisis, name = 'aboutwhateverthisis'),
    path('contactus', contactus, name='contactus'),
    path('reviews', reviews, name='reviews'),
    path('booking', booking, name='booking'),
    path('<slug:slug>/', topic_detail, name='topic_detail'),
    path('login', loginpage, name = 'loginpage'),
    path('exitlog', logoutuser, name = 'logoutuser'),
    path('register', register, name = 'register'),
]
