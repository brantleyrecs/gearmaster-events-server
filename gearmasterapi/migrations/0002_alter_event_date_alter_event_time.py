# Generated by Django 4.1.3 on 2024-02-17 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gearmasterapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='time',
            field=models.TimeField(),
        ),
    ]
