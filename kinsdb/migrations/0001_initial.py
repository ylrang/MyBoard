# Generated by Django 4.2.8 on 2023-12-29 05:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BRNC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('system', models.CharField(max_length=10)),
                ('nation', models.CharField(max_length=10)),
                ('doc_id', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('file', models.FileField(blank=True, null=True, upload_to='brnc/')),
            ],
        ),
        migrations.CreateModel(
            name='UNIST',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('evaluation', models.CharField(max_length=100)),
                ('develop', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=200)),
                ('nation', models.CharField(max_length=10)),
                ('background', models.TextField()),
                ('regulation', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='unist/')),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('institute', models.CharField(max_length=10)),
                ('report_title', models.CharField(max_length=100)),
                ('file', models.FileField(blank=True, null=True, upload_to='unist/report/')),
                ('case_title', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='kinsdb.unist')),
            ],
        ),
        migrations.CreateModel(
            name='Related',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_reviewed', models.CharField(max_length=100)),
                ('section_reviewed', models.CharField(max_length=200)),
                ('report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_report', to='kinsdb.report')),
            ],
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('summary', models.TextField()),
                ('proposal', models.TextField()),
                ('category', models.CharField(max_length=100)),
                ('report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='issues', to='kinsdb.report')),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institute', models.CharField(max_length=10)),
                ('title', models.CharField(max_length=200)),
                ('index', models.CharField(max_length=100)),
                ('index_title', models.CharField(max_length=100)),
                ('index_title_kr', models.CharField(max_length=100)),
                ('index_content', models.TextField()),
                ('index_content_kr', models.TextField()),
                ('sector', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('brnc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='regulation_doc', to='kinsdb.brnc')),
            ],
            options={
                'ordering': ('brnc__doc_id', 'title', 'index'),
            },
        ),
    ]