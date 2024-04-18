# Generated by Django 5.0.3 on 2024-03-13 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=70, verbose_name='Nome')),
                ('descricao', models.TextField(blank=True, null=True, verbose_name='Descrição')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=19, verbose_name='Valor R$')),
                ('comissao', models.DecimalField(decimal_places=2, max_digits=19, verbose_name='Comissão R$')),
            ],
            options={
                'verbose_name': 'Serviço',
                'verbose_name_plural': 'Serviços',
                'ordering': ['nome'],
            },
        ),
    ]
