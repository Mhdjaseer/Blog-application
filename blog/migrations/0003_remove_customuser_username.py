# Generated by Django 4.2.3 on 2023-07-05 16:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_like'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='username',
        ),
    ]