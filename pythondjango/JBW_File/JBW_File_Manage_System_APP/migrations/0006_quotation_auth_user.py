# Generated by Django 4.0.2 on 2022-05-23 07:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('JBW_File_Manage_System_APP', '0005_remove_quotation_auth_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='quotation',
            name='auth_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
