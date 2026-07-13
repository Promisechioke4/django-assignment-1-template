from django.contrib import admin
from .models import Skill, BlogPost, ContactMessage, Project

class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'proficiency')

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')

class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'submitted_at')

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'tech_stack', 'created_at')

admin.site.register(Skill, SkillAdmin)
admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(ContactMessage, ContactMessageAdmin)
admin.site.register(Project, ProjectAdmin)