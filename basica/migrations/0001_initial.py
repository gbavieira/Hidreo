# Generated by Django 4.0.4 on 2022-05-05 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('telefone', models.CharField(max_length=20)),
                ('cpf_cnpj', models.CharField(max_length=17)),
                ('concessionaria', models.CharField(max_length=50)),
                ('data', models.DateTimeField(verbose_name='Data do Orçamento')),
                ('email', models.CharField(max_length=20)),
                ('modelo', models.CharField(max_length=20)),
                ('desnivel', models.IntegerField()),
                ('vazao', models.IntegerField()),
                ('potencia', models.IntegerField()),
                ('mchs', models.IntegerField()),
            ],
        ),
    ]
