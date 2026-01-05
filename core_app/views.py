from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, logout # login - Вход, logout - Выход
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required # Авторизация обязательно
from .models import Post
from .forms import  PostForm

def register_view(request):
    if request.user.is_authenticated:
        return redirect('post_list')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_view')
    else:
        form = UserCreationForm()

    context = {
        'form': form
    }
    return render(request, 'register.html', context)


def login_view(request):
        if request.user.is_authenticated:
            return redirect('post_list')

        if request.method == 'POST':
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                user = form.get_user()
                login(request, user)
                return redirect('post_list')
        else:
            form = AuthenticationForm()
        context = {
            'form': form
        }
        return render(request, 'login.html', context)

def logout_view(request):
    logout(request)
    return redirect('login-view')

def post_list(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'posts.html', context)

@login_required(login_url='login_view')
def create_post_view(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    context = {
        'form': form
    }
    return render(request, 'post_form.html', context)


def update_post_view(request, pk):
    post = get_object_or_404(Post, pk=pk, user=request.user)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm(instance=post)
        context = {
            'form': form
        }
    return render(request, 'post_form.html', {'form': form})

@login_required(login_url='login_view')
def delete_post_view(request, pk):
    post = get_object_or_404(Post, pk=pk, user=request.user)
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')
    context = {
        'post': post
    }
    return render(request, 'delete.html', context)


