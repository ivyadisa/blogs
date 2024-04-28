from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def upload_blogs(request):
    
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        picture = request.POST.get('image')
        category = request.POST.get('category')

        blogs, created = Blogs.objects.get_or_create(title=title, content=content, picture=picture, category=category)

        messages.success(request, "Blog uploaded successfully")
        return redirect('blogs')
    
    return render(request, 'uploads.html')

@login_required
def delete_blogs(request, blog_id):
    blog_post = get_object_or_404(Blogs, id=blog_id)
    
    if request.method == 'POST':
        blog_post.delete()
        messages.success(request, "Blog deleted successfully")
        return redirect('blogs')
    
    return render(request, 'delete-blogs.html', {"blog_post":blog_post})

@login_required
def edit_blogs(request, blog_id):
    blog_post = get_object_or_404(Blogs, id=blog_id)
    
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        new_picture = request.POST.get('image')
        category = request.POST.get('category')
        
        if new_picture:
            if blog_post.picture:
                blog_post.picture.delete()
            blog_post.picture = new_picture
        
        blog_post.title = title
        blog_post.content = content
        blog_post.category = category
        blog_post.save()
        
        messages.success(request, "Blog updated successfully")
        return redirect('blog-detail', blog_id=blog_id) 
    
    return render(request, 'edit-blogs.html', {"blog_post": blog_post})

def list_blogs(request):
    blogs = Blogs.objects.all().order_by('-uploaded_on')
    return render(request, 'blogs.html', {'blogs':blogs})

def detail_blogs(request, blog_id):
    blog_post = get_object_or_404(Blogs, id=blog_id)

    comment_list = Comments.objects.filter(blog_post=blog_post).order_by('-commented_on')

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.blog_post = blog_post
            comment.save()
            messages.success(request, "Blog commented successfully")
            return redirect('blog-detail', blog_id)
        else:
            messages.success(request, "Error commenting Blog")
    else:
        comment_form = CommentForm()
        
    return render(request, "blog-details.html", {"blog_post": blog_post, 'comment_form':comment_form, 'comment_list':comment_list})

@login_required
def dashboard_view(request):
    return render(request, 'dashboard.html')

def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully")
            return redirect('login')
        else:
            messages.success(request, "Error creating account")
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {"form" : form})