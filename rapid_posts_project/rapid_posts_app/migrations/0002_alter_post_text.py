# Generated by Django 5.0.7 on 2024-08-05 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rapid_posts_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.CharField(max_length=500),
        ),
    ]
