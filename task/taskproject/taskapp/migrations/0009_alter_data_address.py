# Generated by Django 4.1.4 on 2023-02-11 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0008_alter_data_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='address',
            field=models.TextField(max_length=10),
        ),
    ]
