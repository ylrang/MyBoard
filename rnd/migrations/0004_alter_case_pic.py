# Generated by Django 4.2.8 on 2024-01-24 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rnd', '0003_case_published_alter_case_created_alter_case_updated_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='PIC',
            field=models.CharField(default='홍길동', max_length=100),
        ),
    ]
