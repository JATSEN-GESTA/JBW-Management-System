# Generated by Django 4.0.2 on 2022-05-22 12:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('JBW_File_Manage_System_APP', '0002_quotation_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quotation',
            name='order_num',
        ),
    ]
