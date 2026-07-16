from django.db import models
from django.utils.text import slugify

class Skill(models.Model):
    # Category choices display as human-readable names on the admin dashboard,
    # but store the short code (e.g., 'Frontend') in the database.
    CATEGORY_CHOICES = [
        ('Frontend', 'Frontend Development'),
        ('Backend', 'Backend Development'),
        ('Database', 'Database Management'),
        ('Devops', 'DevOps & Tools'),
        ('Soft Skills', 'Soft Skills'),
        ('Other', 'Other Tech Stack'),
    ]

    name = models.CharField(max_length=100, help_text="Enter the skill name (e.g., Python, React)")
    percentage = models.IntegerField(
        help_text="Enter proficiency level as percentage (0-100)"
    )
    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default='Frontend',
        help_text="Select the category for this skill"
    )

    def __str__(self):
        # This defines how a Skill object is represented as a string (e.g., in the admin panel)
        return f"{self.name} ({self.percentage}%)"

    class Meta:
        # Sorts skills by percentage in descending order by default
        ordering = ['-percentage']


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically record time when message is sent

    def __str__(self):
        return f"Message from {self.name} - {self.subject}"

    class Meta:
        ordering = ['-created_at']  # Newest messages show first


class BlogPost(models.Model):
    title = models.CharField(max_length=200, help_text="Title of the blog post")
    # A slug is a clean URL representation (e.g. 'my-first-post' instead of '?id=5')
    slug = models.SlugField(unique=True, blank=True, help_text="SEO URL slug. Generated automatically if blank.")
    content = models.TextField(help_text="Main content of the blog post")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  # Updates automatically on edit

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # Override save() to automatically create a clean slug from the title if not provided
        if not self.slug:
            self.slug = slugify(self.title)
            # Ensure the slug is unique by appending numbers if a duplicate exists
            original_slug = self.slug
            count = 1
            while BlogPost.objects.filter(slug=self.slug).exists():
                self.slug = f"{original_slug}-{count}"
                count += 1
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-created_at']
