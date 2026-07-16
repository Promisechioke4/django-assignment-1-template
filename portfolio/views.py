from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Skill, Contact, BlogPost
from .forms import ContactForm, BlogPostForm

# 1. HOMEPAGE VIEW
def home(request):
    """
    Renders the landing page. We also query the top 3 skills and latest 2 blog posts
    to make the homepage dynamic and content-rich.
    """
    skills = Skill.objects.all().order_by('-percentage')[:3]
    latest_posts = BlogPost.objects.all()[:2]
    context = {
        'skills': skills,
        'latest_posts': latest_posts
    }
    return render(request, 'portfolio/home.html', context)


# 2. SKILL PAGE VIEW
def skills_page(request):
    """
    Fetches all skills from the database and passes them as a flat list.
    Skills are uploaded from the admin dashboard and displayed on the frontend.
    """
    skills = Skill.objects.all().order_by('-percentage')
    context = {
        'skills': skills,
    }
    return render(request, 'portfolio/skills.html', context)


# 3. CONTACT PAGE VIEW
def contact_page(request):
    """
    Handles the contact form.
    - If GET: Renders a blank form.
    - If POST: Receives form data, validates it, and saves it to the database.
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Saves contact message to the database
            messages.success(request, "Your message has been sent successfully! Thank you.")
            return redirect('contact')  # Redirects back to contact page to clear form fields
        else:
            messages.error(request, "There was an error in your form. Please check the fields below.")
    else:
        form = ContactForm()

    context = {
        'form': form
    }
    return render(request, 'portfolio/contact.html', context)


# 4. BLOG PAGE - READ ALL (List)
def blog_list(request):
    """
    Lists all blog posts in descending order of creation.
    """
    posts = BlogPost.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'portfolio/blog_list.html', context)


# 5. BLOG PAGE - READ ONE (Detail)
def blog_detail(request, slug):
    """
    Displays a single blog post using its unique slug.
    """
    post = get_object_or_404(BlogPost, slug=slug)
    context = {
        'post': post
    }
    return render(request, 'portfolio/blog_detail.html', context)


# 6. BLOG PAGE - CREATE
def blog_create(request):
    """
    Handles creating a new blog post.
    """
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            post = form.save()  # Automatically slugifies and saves
            messages.success(request, f'Blog post "{post.title}" created successfully!')
            return redirect('blog_detail', slug=post.slug)
    else:
        form = BlogPostForm()

    context = {
        'form': form,
        'title': 'Create New Blog Post',
        'button_text': 'Publish Post'
    }
    return render(request, 'portfolio/blog_form.html', context)


# 7. BLOG PAGE - UPDATE (Edit)
def blog_update(request, slug):
    """
    Handles updating an existing blog post.
    """
    post = get_object_or_404(BlogPost, slug=slug)
    
    if request.method == 'POST':
        # Pass instance=post so the form updates the existing record instead of creating a new one
        form = BlogPostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            messages.success(request, f'Blog post "{post.title}" updated successfully!')
            return redirect('blog_detail', slug=post.slug)
    else:
        # Pre-populates the form with existing blog post data
        form = BlogPostForm(instance=post)

    context = {
        'form': form,
        'title': f'Edit Post: {post.title}',
        'button_text': 'Save Changes',
        'post': post
    }
    return render(request, 'portfolio/blog_form.html', context)


# 8. BLOG PAGE - DELETE
def blog_delete(request, slug):
    """
    Handles deleting a blog post with a confirmation step.
    """
    post = get_object_or_404(BlogPost, slug=slug)
    
    if request.method == 'POST':
        title = post.title
        post.delete()  # Removes post from database
        messages.success(request, f'Blog post "{title}" deleted successfully.')
        return redirect('blog_list')
        
    context = {
        'post': post
    }
    return render(request, 'portfolio/blog_confirm_delete.html', context)
