# Generated by Django 4.1.4 on 2022-12-07 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='fornecedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nome', models.CharField(max_length=50)),
                ('CNPJ', models.CharField(max_length=15)),
                ('Contato', models.CharField(max_length=11)),
                ('Produto', models.CharField(max_length=100)),
                ('Quantidade', models.CharField(max_length=10)),
            ],
        ),
    ]
