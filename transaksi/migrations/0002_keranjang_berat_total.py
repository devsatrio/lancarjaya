# Generated by Django 2.2 on 2020-02-13 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaksi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='keranjang',
            name='berat_total',
            field=models.IntegerField(default=0),
        ),
    ]
