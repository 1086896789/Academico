# Generated by Django 4.2.5 on 2023-11-08 01:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0011_countries'),
    ]

    operations = [
        migrations.AddField(
            model_name='persons',
            name='id_User',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='students.user'),
        ),
    ]
