from django.shortcuts import render, redirect, get_object_or_404
from .models import Skill, BlogPost, Project
from .forms import BlogPostForm, ContactForm

def home(request):
    return render(request, 'home.html')

def skills(request):
    all_skills = Skill.objects.all()
    return render(request, 'skills.html', {'skills': all_skills})


# ── Blog CRUD views ────────────────────────────────────────────

def blog_list(request):
    posts = BlogPost.objects.all().order_by('-created_at')
    return render(request, 'blog_list.html', {'posts': posts})


def blog_detail(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    return render(request, 'blog_detail.html', {'post': post})


def blog_create(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog_list')
    else:
        form = BlogPostForm()
    return render(request, 'blog_form.html', {'form': form})


def blog_update(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog_detail', post_id=post.id)
    else:
        form = BlogPostForm(instance=post)
    return render(request, 'blog_form.html', {'form': form})


def blog_delete(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    post.delete()
    return redirect('blog_list')


# ── Contact view ─────────────────────────────────────────────

def contact(request):
    submitted = False  # tracks whether we should show a "thank you" message

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # saves the visitor's message into the database
            submitted = True
            form = ContactForm()  # reset to a blank form after saving
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form, 'submitted': submitted})

def projects(request):
    all_projects = Project.objects.all().order_by('-created_at')
    return render(request, 'projects.html', {'projects': all_projects})