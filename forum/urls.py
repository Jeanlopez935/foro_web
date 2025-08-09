from django.urls import path
from .views import PostListView, CategoryDetailView

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
]