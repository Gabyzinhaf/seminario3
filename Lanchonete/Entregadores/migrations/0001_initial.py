# Generated by Django 4.1.4 on 2022-12-07 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='entregador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nome', models.CharField(max_length=50)),
                ('Endereco', models.CharField(max_length=50)),
                ('Veiculo', models.CharField(max_length=20)),
                ('Placa', models.CharField(max_length=7)),
                ('CNH', models.CharField(max_length=9)),
            ],
        ),
    ]
