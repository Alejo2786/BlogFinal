import requests
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import RegistrationForm, CommentForm
from .models import Post, Comment, Repost
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView,  LogoutView
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .analytics import fetch_posts_data, plot_post_counts, plot_user_comment_distribution



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
    query_user = request.GET.get('user', '')  # Establece un valor predeterminado en blanco si es None
    query_content = request.GET.get('content', '')  # Establece un valor predeterminado en blanco si es None
    query_date = request.GET.get('date', '')  # Establece un valor predeterminado en blanco si es None
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

@login_required
def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comments = Comment.objects.filter(post=post)
    reposts = Repost.objects.filter(post=post)
    user_has_reposted = Repost.objects.filter(user=request.user, post=post).exists()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment_text = form.cleaned_data['text']
            Comment.objects.create(user=request.user, post=post, text=comment_text)
    else:
        form = CommentForm()

    return render(request, 'post_detail.html', {'post': post, 'comments': comments, 'reposts': reposts, 'user_has_reposted': user_has_reposted, 'form': form})



@login_required
def repost_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    user_has_reposted = Repost.objects.filter(user=request.user, post=post).exists()

    if not user_has_reposted:
        Repost.objects.create(user=request.user, post=post)

    return redirect('post_detail', post_id=post_id)




def post_counts(request):
    # Obtén los datos de las publicaciones
    df_posts = fetch_posts_data()

    if df_posts is not None:
        # Si se obtuvieron datos, crea la gráfica y obtén la imagen en base64
        image_base64 = plot_post_counts(df_posts)

    # Renderiza el template y pasa la imagen en base64 como contexto
    return render(request, 'post_statistics.html', {'image_base64': image_base64})


def user_comment_distribution(request):
    # Obtén la imagen en formato base64 desde la función de analytics.py
    image_base64 = plot_user_comment_distribution()

    # Renderiza el template y pasa la imagen base64 como contexto
    return render(request, 'user_comment_distribution.html', {'image_base64': image_base64})