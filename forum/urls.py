from django.urls import path
from .views import PostListView, CategoryDetailView, PostCreateView, PostUpdateView, PostDeleteView, RegisterView
from django.views.generic import TemplateView
from .views import ProfileView
from .views import PostDetailView

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('register/', RegisterView.as_view(), name='register'),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
]
