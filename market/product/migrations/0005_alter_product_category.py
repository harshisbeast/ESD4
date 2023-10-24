# Generated by Django 4.2.6 on 2023-10-24 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('vegetables', 'vegetables'), ('fruits', 'fruits'), ('meat', 'meat')], default='Select a category', max_length=25),
        ),
    ]
