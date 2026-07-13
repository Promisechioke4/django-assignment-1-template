from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('skills/', views.skills, name='skills'),
    path('projects/', views.projects, name='projects'),

    path('blog/', views.blog_list, name='blog_list'),
    path('blog/<int:post_id>/', views.blog_detail, name='blog_detail'),
    path('blog/create/', views.blog_create, name='blog_create'),
    path('blog/<int:post_id>/edit/', views.blog_update, name='blog_update'),
    path('blog/<int:post_id>/delete/', views.blog_delete, name='blog_delete'),

    path('contact/', views.contact, name='contact'),
]