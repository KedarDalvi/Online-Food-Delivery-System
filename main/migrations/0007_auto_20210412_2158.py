# Generated by Django 3.0.6 on 2021-04-12 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_detail_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detail',
            name='username',
            field=models.CharField(default='kedar', max_length=100),
        ),
    ]
