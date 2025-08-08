from django.urls import path
from . import views

app_name = 'forum'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('category/<int:category_id>/', views.category_detail, name='category_detail'),
]