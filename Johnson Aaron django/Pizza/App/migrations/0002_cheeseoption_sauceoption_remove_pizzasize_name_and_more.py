
# Generated by Django 4.1.5 on 2023-02-06 20:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CheeseOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cheese', models.CharField(default='mozzerella', max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='SauceOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sauce', models.CharField(default='tomato', max_length=32)),
            ],
        ),
        migrations.RemoveField(
            model_name='pizzasize',
            name='name',
        ),
        migrations.RemoveField(
            model_name='pizzasize',
            name='price',
        ),
        migrations.AddField(
            model_name='pizzasize',
            name='size',
            field=models.CharField(default='medium', max_length=32),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='cheese',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.cheeseoption'),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='sauce',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.sauceoption'),
        ),
        migrations.DeleteModel(
            name='Cheese',
        ),
        migrations.DeleteModel(
            name='Sauce',
        ),
    ]
