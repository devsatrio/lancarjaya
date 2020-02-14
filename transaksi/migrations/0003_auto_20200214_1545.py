# Generated by Django 2.2 on 2020-02-14 15:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('transaksi', '0002_keranjang_berat_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='keranjang',
            name='kode_transaksi',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.CreateModel(
            name='transaksi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kode_transaksi', models.CharField(max_length=150, null=True)),
                ('subtotal', models.IntegerField(default=0)),
                ('ongkir', models.IntegerField(default=0)),
                ('berat_total', models.IntegerField(default=0)),
                ('total_biaya', models.IntegerField(default=0, null=True)),
                ('tanggal_beli', models.DateTimeField(auto_now_add=True)),
                ('opsi_pengiriman', models.CharField(max_length=150, null=True)),
                ('status_verifikasi', models.BooleanField(default=False)),
                ('tanggal_verivikasi', models.DateTimeField(null=True)),
                ('resi_pengiriman', models.CharField(max_length=150, null=True)),
                ('pembeli', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
