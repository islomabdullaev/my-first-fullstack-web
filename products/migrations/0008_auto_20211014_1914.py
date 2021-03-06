# Generated by Django 3.2.7 on 2021-10-14 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_alter_productmodel_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='price',
            field=models.FloatField(null=True, verbose_name='price'),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='real_price',
            field=models.FloatField(blank=True, default=0, verbose_name='real price'),
        ),
    ]
