# Generated by Django 3.2.15 on 2022-10-25 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prescriptions', '0003_auto_20221006_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prescription',
            name='frequency',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]