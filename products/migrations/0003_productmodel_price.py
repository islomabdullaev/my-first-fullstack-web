# Generated by Django 3.2.7 on 2021-10-14 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20211013_0359'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='price',
            field=models.FloatField(null=True, verbose_name='price'),
        ),
    ]
