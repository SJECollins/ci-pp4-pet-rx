# Generated by Django 3.2.15 on 2022-09-30 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vetprofiles', '0004_alter_vet_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vet',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
