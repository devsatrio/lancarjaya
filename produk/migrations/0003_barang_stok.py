# Generated by Django 2.2 on 2020-02-07 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produk', '0002_auto_20200206_0815'),
    ]

    operations = [
        migrations.AddField(
            model_name='barang',
            name='stok',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
