# Generated by Django 3.1 on 2022-12-04 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userentry', '0003_auto_20221204_1254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.IntegerField(default=0),
        ),
    ]
