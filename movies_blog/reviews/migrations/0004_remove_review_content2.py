# Generated by Django 4.2.11 on 2024-04-16 09:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_reviewlikeusers_review_like_users'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='content2',
        ),
    ]