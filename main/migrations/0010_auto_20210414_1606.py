# Generated by Django 3.0.6 on 2021-04-14 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_order_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detail',
            name='dict_item',
            field=models.TextField(null=True),
        ),
    ]
