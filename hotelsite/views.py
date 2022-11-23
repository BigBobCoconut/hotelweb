from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CommentForm, CreateUserForm
from .models import Topic
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout               

def mainpage(request):
    if request.user.is_authenticated:
        print("haha")
    return render(request, "base.html",)

def aboutwhatthisis(request):
    return render(request, "about.html")

def contactus(request):
    return render(request, "contactus.html")

def reviews(request):
    topics = Topic.objects.all()
    form = CommentForm(request.POST)

    return render(request, 'reviews.html', {'topics': topics, 'form': form, })

def booking(request):
    return render(request, "booking.html")

def logoutuser(request):
    logout(request)
    return redirect('loginpage')

def loginpage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('mainpage')

    context = {"form": form}
    return render(request, "login.html", context)


def register(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('loginpage')
    
    context = {"form": form}
    return render(request, "register.html", context)

def topic_detail(request, slug):
    topic = Topic.objects.get(slug=slug)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.topic = topic
            comment.save()

            return redirect('topic_detail', slug=topic.slug)
    else:
        form = CommentForm()

    return render(request, 'topic_detail.html', {'topic': topic, 'form': form})
