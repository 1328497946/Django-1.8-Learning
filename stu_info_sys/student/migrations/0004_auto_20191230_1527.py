# Generated by Django 2.1.7 on 2019-12-30 07:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_auto_20191230_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='NAME_DEP',
            field=models.CharField(default='', max_length=50, verbose_name='全称'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='student',
            name='NAME_DEP',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.DEPARTMENT', verbose_name='院系'),
        ),
    ]
