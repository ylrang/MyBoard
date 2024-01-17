# Generated by Django 4.2.8 on 2024-01-16 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kinsdb', '0011_alter_unist_epg'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='unist',
            name='evluation',
        ),
        migrations.RemoveField(
            model_name='unist',
            name='evluation1',
        ),
        migrations.RemoveField(
            model_name='unist',
            name='evluation2',
        ),
        migrations.RemoveField(
            model_name='unist',
            name='evluation3',
        ),
        migrations.AddField(
            model_name='unist',
            name='eval1',
            field=models.CharField(choices=[('1', 'Safety Context'), ('2', '안전전략'), ('3', '평가 베이시스'), ('4', '안전성 평가'), ('5', '관리 시스템/이해관계자 및 규제기관 참여'), ('6', '증거들의 종합'), ('7', '불확실성 관리'), ('8', '한계점, 통제 및 조건')], default=1, max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='unist',
            name='eval2',
            field=models.CharField(default='1', max_length=2),
        ),
        migrations.AddField(
            model_name='unist',
            name='evaluation',
            field=models.CharField(choices=[('1', 'Safety Context'), ('2', '안전전략'), ('3', '평가 베이시스'), ('4', '안전성 평가'), ('5', '관리 시스템/이해관계자 및 규제기관 참여'), ('6', '증거들의 종합'), ('7', '불확실성 관리'), ('8', '한계점, 통제 및 조건')], default='1', max_length=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='unist',
            name='develop',
            field=models.CharField(choices=[('1', '개념화'), ('2', '부지조사/선정'), ('3', '기준 설계/인허가 신청'), ('4', '건설'), ('5', '운영'), ('6', '폐쇄')], max_length=2),
        ),
    ]