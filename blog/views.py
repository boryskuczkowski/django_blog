from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.db.models import Q
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.urls import reverse
from .models import Post
from category.models import Category
from .forms import PostFormModel


class PostListView(ListView):
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):

        qs = Post.objects.all()
        query = self.request.GET.get("q", None)

        if query is not None:
            qs = qs.filter(
                Q(title__unaccent__icontains=query) |
                Q(content__unaccent__icontains=query) |
                Q(author__username__unaccent__icontains=query) |
                Q(date_posted__icontains=query)
            ).distinct()
        return qs.order_by('-date_posted')


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        qs = Post.objects.filter(author=user).order_by('-date_posted')
        query = self.request.GET.get("q", None)
        if query is not None:
            qs = qs.filter(
                Q(title__unaccent__icontains=query) |
                Q(content__unaccent__icontains=query) |
                Q(author__username__unaccent__icontains=query) |
                Q(date_posted__icontains=query)
            ).distinct()

        return qs.order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostFormModel

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostFormModel

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    context = {
        'title': 'AB out Baking',
    }
    return render(request, 'blog/about.html', context)
