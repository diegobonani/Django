# Generated by Django 3.1.5 on 2021-02-08 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CadastroPessoas',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=50)),
                ('sobrenome', models.CharField(max_length=50)),
                ('idade', models.IntegerField()),
                ('data_nascimento', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('apelido', models.CharField(max_length=40)),
                ('observacao', models.TextField()),
            ],
        ),
    ]
