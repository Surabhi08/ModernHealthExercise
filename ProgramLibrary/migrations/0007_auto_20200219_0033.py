# Generated by Django 3.0.3 on 2020-02-19 00:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ProgramLibrary', '0006_auto_20200219_0004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='program',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ProgramLibrary.Program'),
        ),
    ]
