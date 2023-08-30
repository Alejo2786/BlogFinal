import requests
from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import UserProfile, Post
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView,  LogoutView
from django.contrib.auth.decorators import login_required
from django.db.models import Q


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Guarda el usuario automáticamente
            return redirect('login')  # Redirecciona a la página de inicio de sesión
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

def custom_logout(request):
    return LogoutView.as_view()(request)

def custom_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Redirecciona a la página después del inicio de sesión exitoso
    return LoginView.as_view()(request)

def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def create_post(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        author = request.user  # El usuario actual está disponible en request.user
        post = Post(title=title, content=content, author=author)
        post.save()
        return redirect('post_list')
    return render(request, 'create_post.html')

def post_list(request):
    query_user = request.GET.get('user')
    query_content = request.GET.get('content')
    query_date = request.GET.get('date')
    posts = Post.objects.all()

    if query_user:
        posts = posts.filter(author__username__icontains=query_user)
    if query_content:
        posts = posts.filter(content__icontains=query_content)
    if query_date:
        posts = posts.filter(created_at__icontains=query_date)

    return render(request, 'post_list.html', {
        'posts': posts,
        'query_user': query_user,
        'query_content': query_content,
        'query_date': query_date,
    })
