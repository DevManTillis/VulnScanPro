# Generated by Django 2.0.1 on 2018-01-31 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0013_vuln_v_remove_fix'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='document_version',
            field=models.CharField(default='NONE', max_length=200),
        ),
    ]
