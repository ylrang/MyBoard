# Generated by Django 5.0 on 2023-12-18 05:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cloud', '0007_alter_post_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='file_type',
        ),
    ]