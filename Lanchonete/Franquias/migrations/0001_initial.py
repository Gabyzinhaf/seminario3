# Generated by Django 4.1.4 on 2022-12-07 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='franquia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NomeProprietario', models.CharField(max_length=50)),
                ('CNPJ', models.CharField(max_length=15)),
                ('Endereco', models.CharField(max_length=100)),
                ('Email', models.CharField(max_length=100)),
                ('Contato', models.CharField(max_length=11)),
            ],
        ),
    ]
