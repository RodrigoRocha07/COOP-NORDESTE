# Generated by Django 5.1 on 2024-08-28 15:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coop', '0002_locacao_cooperado_locacao'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Locacao',
            new_name='Locação',
        ),
    ]
