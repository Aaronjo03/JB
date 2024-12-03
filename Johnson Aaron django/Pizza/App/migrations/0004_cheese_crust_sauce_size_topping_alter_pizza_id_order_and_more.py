# Generated by Django 4.1.5 on 2023-02-06 21:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_alter_pizzasize_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cheese',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='Mozzerella', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Crust',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='Thin', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Sauce',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='Tomato', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='Medium', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Topping',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='Ham', max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='pizza',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('pizza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.pizza')),
            ],
        ),
        migrations.AddField(
            model_name='pizza',
            name='crust',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.crust'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pizza',
            name='toppings',
            field=models.ManyToManyField(to='App.topping'),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='cheese',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.cheese'),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='sauce',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.sauce'),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='size',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.size'),
        ),
        migrations.DeleteModel(
            name='CheeseOption',
        ),
        migrations.DeleteModel(
            name='PizzaSize',
        ),
        migrations.DeleteModel(
            name='SauceOption',
        ),
    ]
