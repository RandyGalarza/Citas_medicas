# Generated by Django 4.2.6 on 2023-10-21 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cita_medica', '0003_cita'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='alergias',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Polen'), (2, 'Polvo'), (3, 'Otro')], default=0),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='estado',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
