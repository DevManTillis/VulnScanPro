# Generated by Django 2.0 on 2018-01-03 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0002_vuln_v_fin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vuln',
            name='v_com',
            field=models.CharField(default='NONE', max_length=200),
        ),
        migrations.AlterField(
            model_name='vuln',
            name='v_con',
            field=models.CharField(default='NONE', max_length=200),
        ),
        migrations.AlterField(
            model_name='vuln',
            name='v_det',
            field=models.CharField(default='NONE', max_length=200),
        ),
        migrations.AlterField(
            model_name='vuln',
            name='v_dis',
            field=models.CharField(default='NONE', max_length=200),
        ),
        migrations.AlterField(
            model_name='vuln',
            name='v_fix',
            field=models.CharField(default='NONE', max_length=200),
        ),
        migrations.AlterField(
            model_name='vuln',
            name='v_ref',
            field=models.CharField(default='NONE', max_length=200),
        ),
        migrations.AlterField(
            model_name='vuln',
            name='v_sev',
            field=models.CharField(default='NONE', max_length=200),
        ),
        migrations.AlterField(
            model_name='vuln',
            name='v_sta',
            field=models.CharField(default='NONE', max_length=200),
        ),
    ]
