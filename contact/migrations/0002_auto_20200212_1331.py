# Generated by Django 2.2 on 2020-02-12 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='kode_kota',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='kota',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
