# Generated by Django 4.2.5 on 2023-11-15 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0012_persons_id_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='id_person',
            field=models.IntegerField(null=True),
        ),
    ]
