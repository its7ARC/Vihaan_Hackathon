# Generated by Django 3.0.6 on 2020-12-12 08:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_blog_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='rating',
        ),
    ]
