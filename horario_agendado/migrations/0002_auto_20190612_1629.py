# Generated by Django 2.2.2 on 2019-06-12 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servico', '0004_auto_20190612_0913'),
        ('horario_agendado', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='horarioagendado',
            name='servico',
        ),
        migrations.AddField(
            model_name='horarioagendado',
            name='servico',
            field=models.ManyToManyField(to='servico.Servico'),
        ),
    ]