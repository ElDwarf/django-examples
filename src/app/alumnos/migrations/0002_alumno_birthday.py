# Generated by Django 4.0 on 2021-12-16 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumno',
            name='birthday',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
