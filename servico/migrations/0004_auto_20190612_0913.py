# Generated by Django 2.2.2 on 2019-06-12 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servico', '0003_auto_20190612_0908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servico',
            name='id',
            field=models.AutoField(auto_created=True, editable=False, primary_key=True, serialize=False),
        ),
    ]
