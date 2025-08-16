from django.urls import path
from .views import PostListView, CategoryDetailView, PostCreateView, PostUpdateView, PostDeleteView, RegisterView

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('accounts/register/', RegisterView.as_view(), name='register'),
]