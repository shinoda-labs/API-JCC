# Generated by Django 2.2.2 on 2019-06-14 12:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('horario_agendado', '0005_auto_20190613_0907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horarioagendado',
            name='usuario',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, to='usuario.Usuario'),
        ),
    ]
