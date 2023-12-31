# Generated by Django 4.2.6 on 2023-11-12 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cita_medica', '0013_alter_paciente_fecha_registro'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_medico', models.CharField(max_length=100)),
                ('especialidad', models.CharField(max_length=100)),
                ('telefono', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('fecha_nacimiento', models.DateField(blank=True, null=True)),
                ('genero', models.CharField(blank=True, max_length=10, null=True)),
                ('direccion', models.TextField(blank=True, null=True)),
                ('estado', models.CharField(max_length=20)),
                ('fecha_registro', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
