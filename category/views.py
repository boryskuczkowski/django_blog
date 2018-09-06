from django.shortcuts import render
from django.db.models import Q
from django.views.generic import ListView
from blog.models import Post
from .models import Category
from django.shortcuts import render, get_object_or_404
# Create your views here.


class PostCategoryView(ListView):
    model = Post
    template_name = 'category/category.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        self.name = get_object_or_404(Category, name=self.kwargs.get('name'))
        qs = Post.objects.filter(category=self.name).order_by('-date_posted')
        self.qs2 = Category.objects.all()
        query = self.request.GET.get("q", None)
        if query is not None:
            qs = qs.filter(
                Q(title__unaccent__icontains=query) |
                Q(content__unaccent__icontains=query) |
                Q(author__username__unaccent__icontains=query) |
                Q(date_posted__icontains=query)
            ).distinct()

        return qs.order_by('-date_posted')

    def get_context_data(self, **kwargs):
        context = super(PostCategoryView, self).get_context_data(**kwargs)
        context['category'] = self.name
        context['category_list'] = self.qs2
        return context


class PostCategorySidebar(ListView):

    template_name = 'category/sidebar_category.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'

    def get_queryset(self):
        qs = Post.objects.all()
        self.qs2 = Category.objects.all()
        query = self.request.GET.get("q", None)
        if query is not None:
            qs = qs.filter(
                Q(title__unaccent__icontains=query) |
                Q(content__unaccent__icontains=query) |
                Q(author__username__unaccent__icontains=query) |
                Q(date_posted__icontains=query)
            ).distinct()
        return qs.order_by('-date_posted')

    def get_context_data(self, **kwargs):
        context = super(PostCategorySidebar, self).get_context_data(**kwargs)
        context['category_list'] = self.qs2
        return context
