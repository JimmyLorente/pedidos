# Generated by Django 4.1 on 2022-08-12 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0002_crema'),
    ]

    operations = [
        migrations.CreateModel(
            name='Desayuno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('priceM', models.DecimalField(decimal_places=2, max_digits=4)),
                ('priceL', models.DecimalField(decimal_places=2, max_digits=4)),
                ('dImage', models.URLField()),
            ],
        ),
    ]