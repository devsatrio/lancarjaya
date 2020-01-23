# Generated by Django 2.2 on 2020-01-23 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeri', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='foto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul', models.CharField(max_length=50)),
                ('deskripsi', models.TextField(max_length=300)),
                ('gambar', models.ImageField(null=True, upload_to='foto/')),
                ('tanggal', models.DateTimeField(auto_now_add=True, null=True)),
                ('slug', models.SlugField(blank=True, editable=False, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='kategori',
            name='nama_kategori',
        ),
        migrations.AddField(
            model_name='kategori',
            name='nama',
            field=models.CharField(default='', max_length=50, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='kategori',
            name='slug',
            field=models.SlugField(blank=True, editable=False, null=True),
        ),
    ]