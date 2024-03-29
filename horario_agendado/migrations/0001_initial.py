# Generated by Django 2.2.2 on 2019-06-12 14:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('horario', '0001_initial'),
        ('usuario', '0002_auto_20190612_0950'),
        ('servico', '0004_auto_20190612_0913'),
    ]

    operations = [
        migrations.CreateModel(
            name='HorarioAgendado',
            fields=[
                ('id', models.AutoField(auto_created=True, editable=False, primary_key=True, serialize=False)),
                ('data', models.DateField()),
                ('criado', models.DateTimeField(auto_now_add=True)),
                ('confirmado', models.BooleanField(default=False)),
                ('status', models.IntegerField(default=0)),
                ('horario', models.ForeignKey(db_column='id_horario', on_delete=django.db.models.deletion.PROTECT, to='horario.Horario')),
                ('servico', models.ForeignKey(db_column='id_servico', on_delete=django.db.models.deletion.PROTECT, to='servico.Servico')),
                ('usuario', models.ForeignKey(db_column='id_usuario', on_delete=django.db.models.deletion.PROTECT, to='usuario.Usuario')),
            ],
            options={
                'db_table': 'tb_horario_agendado',
            },
        ),
    ]
