# Generated by Django 5.1 on 2024-08-29 18:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coop', '0006_remove_turnotrabalho_cooperado_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TurnoTrabalho',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_inicio', models.DateTimeField()),
                ('data_fim', models.DateTimeField()),
                ('horas_trabalhadas', models.DecimalField(decimal_places=2, max_digits=5)),
                ('valor_por_hora', models.DecimalField(decimal_places=2, max_digits=10)),
                ('observacoes', models.TextField(blank=True, null=True)),
                ('cooperado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='turnos', to='coop.cooperado')),
                ('locacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='turnos', to='coop.locacao')),
            ],
            options={
                'verbose_name': 'Turno de Trabalho',
                'verbose_name_plural': 'Turnos de Trabalho',
                'ordering': ['data_inicio'],
            },
        ),
        migrations.CreateModel(
            name='Pagamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_pagamento', models.DateField(auto_now_add=True)),
                ('valor', models.DecimalField(decimal_places=2, editable=False, max_digits=10)),
                ('observacoes', models.TextField(blank=True, null=True)),
                ('cooperado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pagamentos', to='coop.cooperado')),
                ('referencia_turno', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pagamentos', to='coop.turnotrabalho')),
            ],
            options={
                'verbose_name': 'Pagamento',
                'verbose_name_plural': 'Pagamentos',
                'ordering': ['data_pagamento'],
            },
        ),
    ]
