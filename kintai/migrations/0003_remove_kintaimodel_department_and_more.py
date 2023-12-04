# Generated by Django 4.2.7 on 2023-12-03 09:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kintai', '0002_employee_position_remove_kintaimodel_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kintaimodel',
            name='department',
        ),
        migrations.RemoveField(
            model_name='kintaimodel',
            name='position',
        ),
        migrations.AddField(
            model_name='employee',
            name='department',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='kintai.department', verbose_name='部署名'),
        ),
        migrations.AddField(
            model_name='employee',
            name='position',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='kintai.position', verbose_name='役職名'),
        ),
    ]
