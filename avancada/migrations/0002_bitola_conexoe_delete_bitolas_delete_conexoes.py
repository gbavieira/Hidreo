# Generated by Django 4.0.4 on 2022-05-05 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avancada', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bitola',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bitola', models.CharField(max_length=50)),
                ('corrente', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Conexoe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_conex', models.CharField(max_length=50)),
                ('k', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Bitolas',
        ),
        migrations.DeleteModel(
            name='Conexoes',
        ),
    ]
