# Generated by Django 5.0.3 on 2024-03-18 21:45

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geral', '0002_mecanico'),
        ('servicos', '0002_servico_oficina'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrdemServico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cliente', models.CharField(max_length=100, verbose_name='Cliente')),
                ('veiculo', models.CharField(help_text='Ex: Honda Fan 160', max_length=100, verbose_name='Veículo')),
                ('placa', models.CharField(help_text='Ex: AAA-0B00', max_length=8, verbose_name='Placa')),
                ('previsao', models.DateField(default=datetime.datetime.now, verbose_name='Previsão')),
                ('data_entrada', models.DateTimeField(auto_now=True, verbose_name='Data/Hora Entrada')),
                ('codigo', models.PositiveIntegerField(unique=True, verbose_name='Código OS')),
                ('mecanico', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='geral.mecanico', verbose_name='Mecânico')),
                ('oficina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='geral.oficina', verbose_name='Oficina')),
                ('servico', models.ManyToManyField(related_name='os', to='servicos.servico', verbose_name='Serviços')),
            ],
            options={
                'verbose_name': 'Ordem de Serviço',
                'verbose_name_plural': 'Ordens de Serviços',
                'ordering': ['data_entrada'],
            },
        ),
    ]
