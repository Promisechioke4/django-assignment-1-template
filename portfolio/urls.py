from django.urls import path
from . import views

urlpatterns = [
    # Main pages
    path('', views.home, name='home'),
    path('skills/', views.skills_page, name='skills'),
    path('contact/', views.contact_page, name='contact'),
    
    # Blog CRUD paths
    path('blog/', views.blog_list, name='blog_list'),
    path('blog/create/', views.blog_create, name='blog_create'),
    path('blog/<slug:slug>/', views.blog_detail, name='blog_detail'),
    path('blog/<slug:slug>/edit/', views.blog_update, name='blog_update'),
    path('blog/<slug:slug>/delete/', views.blog_delete, name='blog_delete'),
]
