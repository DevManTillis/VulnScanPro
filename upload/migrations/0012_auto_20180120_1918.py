# Generated by Django 2.0.1 on 2018-01-21 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0011_auto_20180120_1759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vuln',
            name='v_con',
            field=models.CharField(default='NONE', max_length=15000),
        ),
        migrations.AlterField(
            model_name='vuln',
            name='v_dis',
            field=models.CharField(default='NONE', max_length=15000),
        ),
        migrations.AlterField(
            model_name='vuln',
            name='v_fix',
            field=models.CharField(default='NONE', max_length=15000),
        ),
    ]