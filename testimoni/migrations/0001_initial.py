# Generated by Django 2.2 on 2020-02-11 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='testi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254)),
                ('perihal', models.CharField(max_length=100)),
                ('deskripsi', models.TextField()),
                ('tanggal_buat', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
