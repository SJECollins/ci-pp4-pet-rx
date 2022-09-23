# Generated by Django 3.2.15 on 2022-09-23 17:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('records', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Drugs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('dose', models.DecimalField(decimal_places=2, max_digits=4)),
                ('measure', models.CharField(choices=[('ml', 'ml'), ('mg', 'mg')], max_length=2)),
                ('category', models.CharField(choices=[('NSAID', 'NSAID'), ('Antibiotic', 'Antibiotic'), ('Sedative', 'Sedative'), ('Opioid', 'Opioid')], max_length=20)),
                ('route', models.CharField(choices=[('PO', 'PO'), ('IV', 'IV'), ('IM', 'IM'), ('SC', 'SC'), ('Topical', 'Topical')], max_length=8)),
                ('warnings', models.CharField(max_length=300)),
            ],
            options={
                'verbose_name_plural': 'Drugs',
            },
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('animal_weight', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('drug_dose', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('dose', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('measure', models.CharField(blank=True, max_length=2)),
                ('frequency', models.CharField(choices=[('No Repeat', 'No Repeat'), ('SID', 'SID'), ('BID', 'BID'), ('TID', 'TID'), ('Topical', 'Topical')], max_length=10)),
                ('length', models.PositiveIntegerField(default=0)),
                ('route', models.CharField(blank=True, max_length=8)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('animal', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='records.record')),
                ('drug', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='prescriptions.drugs')),
                ('vet', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
