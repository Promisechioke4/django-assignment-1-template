import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_project.settings')
django.setup()

from portfolio.models import Skill

# Clear existing skills and seed with Solomon's real skills
Skill.objects.all().delete()

skills_data = [
    {'name': 'Python',     'percentage': 90, 'category': 'Backend'},
    {'name': 'Django',     'percentage': 88, 'category': 'Backend'},
    {'name': 'HTML',       'percentage': 92, 'category': 'Frontend'},
    {'name': 'CSS',        'percentage': 85, 'category': 'Frontend'},
    {'name': 'Bootstrap',  'percentage': 83, 'category': 'Frontend'},
    {'name': 'JavaScript', 'percentage': 75, 'category': 'Frontend'},
    {'name': 'Git',        'percentage': 80, 'category': 'Devops'},
    {'name': 'GitHub',     'percentage': 80, 'category': 'Devops'},
]

for s in skills_data:
    skill = Skill.objects.create(
        name=s['name'],
        percentage=s['percentage'],
        category=s['category']
    )
    print(f"Created: {skill.name} ({skill.percentage}%) - {skill.category}")

print(f"\nDone! Total skills in database: {Skill.objects.count()}")
