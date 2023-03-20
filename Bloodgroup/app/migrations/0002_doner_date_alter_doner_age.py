# Generated by Django 4.1.7 on 2023-03-10 05:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='doner',
            name='Date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='doner',
            name='Age',
            field=models.IntegerField(),
        ),
    ]
