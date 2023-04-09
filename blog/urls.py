from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='posts_list'),
    path('<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('create/', views.PostCreateView.as_view(), name='create_post'),
    path('<int:pk>/upgrade/', views.PostEditView.as_view(), name='post_edit'),
    path('<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
]
