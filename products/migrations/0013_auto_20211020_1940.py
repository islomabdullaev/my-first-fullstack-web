# Generated by Django 3.2.7 on 2021-10-20 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_auto_20211016_0407'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorymodel',
            name='title_en',
            field=models.CharField(max_length=15, null=True, verbose_name='category'),
        ),
        migrations.AddField(
            model_name='categorymodel',
            name='title_ru',
            field=models.CharField(max_length=15, null=True, verbose_name='category'),
        ),
        migrations.AddField(
            model_name='categorymodel',
            name='title_uz',
            field=models.CharField(max_length=15, null=True, verbose_name='category'),
        ),
        migrations.AddField(
            model_name='colormodel',
            name='title_en',
            field=models.CharField(max_length=32, null=True, verbose_name='code'),
        ),
        migrations.AddField(
            model_name='colormodel',
            name='title_ru',
            field=models.CharField(max_length=32, null=True, verbose_name='code'),
        ),
        migrations.AddField(
            model_name='colormodel',
            name='title_uz',
            field=models.CharField(max_length=32, null=True, verbose_name='code'),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='long_description_en',
            field=models.CharField(max_length=255, null=True, verbose_name='long description'),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='long_description_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='long description'),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='long_description_uz',
            field=models.CharField(max_length=255, null=True, verbose_name='long description'),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='short_description_en',
            field=models.CharField(max_length=255, null=True, verbose_name='short description'),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='short_description_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='short description'),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='short_description_uz',
            field=models.CharField(max_length=255, null=True, verbose_name='short description'),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='title_en',
            field=models.CharField(max_length=50, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='title_ru',
            field=models.CharField(max_length=50, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='title_uz',
            field=models.CharField(max_length=50, null=True, verbose_name='title'),
        ),
    ]