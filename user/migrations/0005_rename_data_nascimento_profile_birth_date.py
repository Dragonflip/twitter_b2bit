# Generated by Django 4.2.1 on 2023-05-25 17:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_rename_nome_profile_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='data_nascimento',
            new_name='birth_date',
        ),
    ]
