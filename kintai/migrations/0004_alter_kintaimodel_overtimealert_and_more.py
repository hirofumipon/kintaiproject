# Generated by Django 4.2.7 on 2023-12-03 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kintai', '0003_remove_kintaimodel_department_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kintaimodel',
            name='overtimealert',
            field=models.CharField(blank=True, default='問題なし', max_length=50, verbose_name='残業警告'),
        ),
        migrations.AlterField(
            model_name='kintaimodel',
            name='reasonforabsense',
            field=models.CharField(blank=True, max_length=50, verbose_name='欠勤理由'),
        ),
    ]
