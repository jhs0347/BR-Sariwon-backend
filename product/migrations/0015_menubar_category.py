# Generated by Django 3.0.3 on 2020-03-03 10:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0014_maincategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='menubar',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.MainCategory'),
        ),
    ]
