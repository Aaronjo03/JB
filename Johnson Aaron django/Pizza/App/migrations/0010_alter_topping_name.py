# Generated by Django 4.1.5 on 2023-02-23 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0009_alter_topping_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topping',
            name='name',
            field=models.CharField(choices=[('Ham', 'Ham'), ('Pepperoni', 'Pepperoni'), ('Pineapple', 'Pineapple')], default='Ham', max_length=20),
        ),
    ]
