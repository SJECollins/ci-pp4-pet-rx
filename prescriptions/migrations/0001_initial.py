# Generated by Django 3.2.15 on 2022-09-21 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Drugs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('dose', models.DecimalField(decimal_places=2, max_digits=4)),
                ('category', models.CharField(choices=[('NSAID', 'NSAID'), ('ANTIBIOTIC', 'Antibiotic'), ('SEDATIVE', 'Sedative'), ('OPIOID', 'Opioid')], max_length=20)),
                ('route', models.CharField(choices=[('IV', 'IV'), ('IM', 'IM'), ('SC', 'SC'), ('TOPICAL', 'Topical')], max_length=8)),
            ],
            options={
                'verbose_name_plural': 'Drugs',
            },
        ),
    ]
