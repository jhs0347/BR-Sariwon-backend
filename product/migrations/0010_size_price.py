# Generated by Django 3.0.3 on 2020-02-25 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_remove_size_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='size',
            name='price',
            field=models.IntegerField(null=True),
        ),
    ]
