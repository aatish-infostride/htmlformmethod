# Generated by Django 4.0.6 on 2022-07-15 21:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registrationapp', '0003_remove_user_rpassword'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='Password',
            new_name='password',
        ),
    ]