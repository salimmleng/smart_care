# Generated by Django 5.0.6 on 2024-07-02 06:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('doctor', '0002_review'),
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointment_status', models.CharField(choices=[('Pending', 'Pending'), ('Completed', 'Completed'), ('Running', 'Running')], max_length=20)),
                ('appointment_types', models.CharField(choices=[('Offline', 'Offline'), ('Online', 'Online')], max_length=20)),
                ('symptom', models.TextField()),
                ('cancel', models.BooleanField(default=False)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.patient')),
                ('time', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='doctor.availabletime')),
            ],
        ),
    ]