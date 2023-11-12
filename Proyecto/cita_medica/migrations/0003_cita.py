# Generated by Django 4.2.6 on 2023-10-21 21:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cita_medica', '0002_rename_fecha_creacion_paciente_fecha_registro_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_cita', models.DateField()),
                ('hora_cita', models.TimeField()),
                ('tipo_cita', models.CharField(max_length=50)),
                ('fecha_registro', models.DateField()),
                ('estado', models.SmallIntegerField()),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cita_medica.paciente')),
            ],
        ),
    ]
