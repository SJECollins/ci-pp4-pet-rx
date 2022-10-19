# Generated by Django 3.2.15 on 2022-10-06 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prescriptions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='drug',
            name='high_dose',
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=4,
                null=True),
        ),
        migrations.AddField(
            model_name='drug',
            name='tablet_strength',
            field=models.CharField(
                blank=True,
                max_length=100),
        ),
        migrations.AddField(
            model_name='drug',
            name='type',
            field=models.CharField(
                choices=[
                    ('Injectable',
                     'Injectable'),
                    ('Liquid',
                     'Liquid'),
                    ('Tablet',
                     'Tablet')],
                default='Injectable',
                max_length=10),
        ),
        migrations.AddField(
            model_name='prescription',
            name='drug_dose_high',
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=4,
                null=True),
        ),
        migrations.AddField(
            model_name='prescription',
            name='type',
            field=models.CharField(
                blank=True,
                max_length=10),
        ),
        migrations.AlterField(
            model_name='prescription',
            name='dose',
            field=models.CharField(
                blank=True,
                max_length=100,
                null=True),
        ),
    ]
