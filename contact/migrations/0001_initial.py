# Generated by Django 2.2 on 2020-02-11 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomer_hp_satu', models.CharField(max_length=20)),
                ('nomer_hp_dua', models.CharField(max_length=20)),
                ('deskripsi', models.TextField()),
                ('alamat', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('instagram', models.CharField(max_length=100)),
                ('facebook', models.CharField(max_length=100)),
                ('moto', models.CharField(max_length=100)),
            ],
        ),
    ]
