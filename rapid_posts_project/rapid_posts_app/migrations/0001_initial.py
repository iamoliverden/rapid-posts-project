# Generated by Django 5.0.7 on 2024-08-05 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=400)),
                ('likesCount', models.IntegerField(default=0)),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='publish date')),
            ],
        ),
    ]
