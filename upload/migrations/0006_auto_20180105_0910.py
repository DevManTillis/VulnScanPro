# Generated by Django 2.0 on 2018-01-05 17:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0005_auto_20180102_1939'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vuln',
            old_name='v_com',
            new_name='Comments',
        ),
        migrations.RenameField(
            model_name='vuln',
            old_name='v_fin',
            new_name='Finding_Details',
        ),
    ]
