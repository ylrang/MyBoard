# Generated by Django 4.2.8 on 2024-01-15 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kinsdb', '0009_unist_assessment3'),
    ]

    operations = [
        migrations.RenameField(
            model_name='unist',
            old_name='assessment1',
            new_name='evluation',
        ),
        migrations.RenameField(
            model_name='unist',
            old_name='assessment2',
            new_name='evluation1',
        ),
        migrations.RenameField(
            model_name='unist',
            old_name='assessment3',
            new_name='evluation2',
        ),
        migrations.AddField(
            model_name='unist',
            name='evluation3',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
