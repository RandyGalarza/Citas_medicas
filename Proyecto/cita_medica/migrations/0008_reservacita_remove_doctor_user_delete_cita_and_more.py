# Generated by Django 4.2.6 on 2023-11-07 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cita_medica', '0007_alter_doctor_options_alter_doctor_managers_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReservaCita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_paciente', models.CharField(max_length=100)),
                ('fecha_cita', models.DateField()),
                ('hora_cita', models.TimeField()),
                ('estado', models.CharField(max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='user',
        ),
        migrations.DeleteModel(
            name='Cita',
        ),
        migrations.DeleteModel(
            name='Doctor',
        ),
        migrations.DeleteModel(
            name='paciente',
        ),
    ]
