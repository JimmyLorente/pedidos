# Generated by Django 4.1 on 2022-08-16 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0005_formulario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
            ],
        ),
    ]
