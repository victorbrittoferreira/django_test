# Generated by Django 3.2.11 on 2022-01-18 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myia', '0004_remove_person_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='phone',
            field=models.CharField(max_length=14),
        ),
    ]
