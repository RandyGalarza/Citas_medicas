# Generated by Django 4.2.6 on 2023-10-23 00:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cita_medica', '0006_doctor_estado_doctor_fecha_registro_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='doctor',
            options={},
        ),
        migrations.AlterModelManagers(
            name='doctor',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='email',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='password',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='user_permissions',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='username',
        ),
        migrations.AddField(
            model_name='doctor',
            name='user',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
