# Generated by Django 2.2.2 on 2019-06-14 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('horario', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horario',
            name='id',
            field=models.AutoField(editable=False, primary_key=True, serialize=False),
        ),
    ]
