# Generated by Django 2.2.2 on 2019-06-12 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id', models.IntegerField(editable=False, primary_key=True, serialize=False)),
                ('horario', models.TimeField(unique=True)),
                ('ativo', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'tb_horario',
            },
        ),
    ]
