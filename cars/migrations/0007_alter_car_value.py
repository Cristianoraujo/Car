# Generated by Django 5.0.7 on 2024-08-26 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0006_alter_car_brand_alter_car_factory_year_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='value',
            field=models.DecimalField(blank=True, decimal_places=3, default=0, max_digits=6, null=True, verbose_name='Valor'),
        ),
    ]
