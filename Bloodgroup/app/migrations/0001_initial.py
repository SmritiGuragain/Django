# Generated by Django 4.1.7 on 2023-03-09 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='doner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
                ('Age', models.IntegerField(max_length=2)),
                ('Category', models.CharField(choices=[('A+ve', 'A+ve'), ('B+ve', 'B+ve'), ('O+ve', 'O+ve'), ('AB+ve', 'AB+ve')], max_length=20)),
            ],
        ),
    ]
