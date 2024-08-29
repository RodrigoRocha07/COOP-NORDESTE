# Generated by Django 5.1 on 2024-08-29 18:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coop', '0003_rename_locacao_locação'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categorias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('tipo', models.CharField(max_length=255)),
                ('atribuição', models.CharField(max_length=255)),
                ('valor_pagamento', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Locacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('categorias', models.ManyToManyField(related_name='locacoes', to='coop.categorias')),
            ],
            options={
                'verbose_name': 'Locação',
                'verbose_name_plural': 'Locações',
                'ordering': ['nome'],
            },
        ),
        migrations.AlterField(
            model_name='cooperado',
            name='locacao',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='coop.locacao'),
        ),
        migrations.DeleteModel(
            name='Locação',
        ),
    ]
