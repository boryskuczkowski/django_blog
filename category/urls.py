from django.urls import path
from .views import PostCategoryView
from . import views


urlpatterns = [
    path('category/<int:pk>/', PostCategoryView.as_view(), name='category-name'),
]
