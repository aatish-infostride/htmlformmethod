# Generated by Django 4.0.5 on 2022-07-13 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrationapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='Rpassword',
            field=models.CharField(max_length=100),
        ),
    ]
