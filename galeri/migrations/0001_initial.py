# Generated by Django 2.2 on 2020-01-23 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='kategori',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_kategori', models.CharField(max_length=50)),
                ('tanggal_buat', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
