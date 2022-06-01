# Generated by Django 4.0.4 on 2022-05-05 22:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bitolas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bitola', models.DecimalField(decimal_places=1, max_digits=5)),
                ('corrente', models.DecimalField(decimal_places=1, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Conexoes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_conex', models.CharField(max_length=50)),
                ('k', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='LeadAvancada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('telefone', models.CharField(max_length=20)),
                ('cpf_cnpj', models.CharField(max_length=17)),
                ('concessionaria', models.CharField(max_length=50)),
                ('data', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('email', models.CharField(max_length=50)),
                ('modelo', models.CharField(max_length=20)),
                ('desnivel', models.IntegerField()),
                ('vazao', models.IntegerField()),
                ('potencia', models.IntegerField()),
                ('mchs', models.IntegerField()),
                ('dist_hidr', models.IntegerField()),
                ('dist_eletr', models.IntegerField()),
            ],
        ),
    ]
