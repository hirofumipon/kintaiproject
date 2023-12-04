# Generated by Django 4.2.7 on 2023-12-03 08:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='部署名')),
            ],
        ),
        migrations.CreateModel(
            name='KintaiModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='従業員名')),
                ('number', models.IntegerField(verbose_name='従業員番号')),
                ('position', models.CharField(max_length=50, verbose_name='役職名')),
                ('checkin', models.DateTimeField(verbose_name='出勤時刻')),
                ('checkout', models.DateTimeField(verbose_name='退勤時刻')),
                ('overtime', models.IntegerField(default=0, verbose_name='残業時間')),
                ('hourlypaycheck', models.IntegerField(verbose_name='時給')),
                ('paycheck', models.IntegerField(verbose_name='本日の給料')),
                ('overtimealert', models.CharField(default='問題なし', max_length=50, verbose_name='残業警告')),
                ('reasonforabsense', models.CharField(max_length=50, verbose_name='欠勤理由')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='kintai.department', verbose_name='部署名')),
            ],
        ),
    ]
