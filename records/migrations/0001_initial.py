# Generated by Django 3.2.15 on 2022-09-25 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField()),
                ('species', models.CharField(choices=[('Canine', 'Canine'), ('Feline', 'Feline')], max_length=10)),
                ('breed', models.CharField(max_length=50)),
                ('sex', models.CharField(choices=[('M', 'M'), ('MN', 'MN'), ('F', 'F'), ('FN', 'FN')], max_length=10)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=5)),
                ('note', models.CharField(max_length=300)),
            ],
            options={
                'ordering': ['surname'],
                'unique_together': {('name', 'surname', 'date_of_birth', 'species', 'breed', 'sex')},
            },
        ),
    ]
