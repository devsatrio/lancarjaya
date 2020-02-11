# Generated by Django 2.2 on 2020-02-07 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produk', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='barang',
            name='gambar',
            field=models.ImageField(blank=True, null=True, upload_to='produk/'),
        ),
        migrations.AddField(
            model_name='barang',
            name='slug',
            field=models.SlugField(editable=False, null=True),
        ),
        migrations.AddField(
            model_name='barang',
            name='status_aktiv',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='kategori',
            name='slug',
            field=models.SlugField(editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='barang',
            name='nama',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='kategori',
            name='nama',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
