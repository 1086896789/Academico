# Generated by Django 4.2.5 on 2023-10-25 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota1', models.CharField(max_length=100)),
                ('nota2', models.CharField(max_length=500)),
            ],
        ),
    ]
