from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy

from eshop_account.models import Profile

from .forms import BlogForm, CommentForm, CategoryForm, EducationForm
from eshop_setting.models import SiteSetting
from .models import Blog, Comment, Education


class EducationView(ListView):
    model = Education
    template_name = "blog-single.html"
    paginate_by = 10


class EducationPage(DetailView):
    model = Education
    template_name = "education.html"


def add_edu(request):
    current_user = request.user
    if request.method == 'POST':
        form = EducationForm(request.POST, request.POST, request.POST)
        if form.is_valid():
            blog = form.save()
            blog.authors.add(current_user)
            blog.save()
            return redirect('/education')
    else:
        form = BlogForm()

    context = {
        'form': form
    }

    return render(request, 'add_blog.html', context)


def add_edu_comment(request, pk):
    if request.method == 'POST':
        current_user = request.user
        form = CommentForm(request.POST)
        for bl in Education.objects.all():
            if bl.pk == pk:
                blog = bl

        if form.is_valid():
            comment = form.save()
            comment.user.add(current_user)
            blog.comments.add(comment)
            blog.save()
            return redirect('/education')
    else:
        form = CommentForm()

    context = {
        'form': form,
    }

    return render(request, 'add_comment.html', context)


class LatestNews(ListView):
    model = Blog
    template_name = "blog.html"
    paginate_by = 10


class BlogPage(DetailView):
    model = Blog
    template_name = "blog_page.html"
# def blog_page(request, blog):
#     comments = blog.comments.all()
#     context = {
#         'comments': comments,
#         'blog': blog
#     }
#     return render(request, 'blog_page.html', context)


# class AddComment(CreateView):
#     model = Comment
#     template_name = "add_comment.html"
#     form_class = CommentForm
#     success_url = reverse_lazy('home_page')
#     def form_valid(self, form):
#         form.instance.user = self.request.user

def add_comment(request, pk):
    if request.method == 'POST':
        current_user = request.user
        form = CommentForm(request.POST)
        for bl in Blog.objects.all():
            if bl.pk == pk:
                blog = bl

        if form.is_valid():
            comment = form.save()
            comment.user.add(current_user)
            blog.comments.add(comment)
            blog.save()
            return redirect('/blog')
    else:
        form = CommentForm()

    context = {
        'form': form,
    }

    return render(request, 'add_comment.html', context)


def news(request):
    site_setting = SiteSetting.objects.first()
    context = {
        'setting': site_setting
    }

    return render(request, 'blog-single.html', context)


def add_blog_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.POST)
        if form.is_valid():
            form.save()
            return redirect('/blog')
    else:
        form = CategoryForm()

    context = {
        'form': form
    }

    return render(request, 'add_blog_category.html', context)


def add_blog(request):
    current_user = request.user
    if request.method == 'POST':
        form = BlogForm(request.POST, request.POST, request.POST)
        if form.is_valid():
            blog = form.save()
            blog.authors.add(current_user)
            blog.save()
            return redirect('/blog')
    else:
        form = BlogForm()

    context = {
        'form': form
    }

    return render(request, 'add_blog.html', context)




