# Generated by Django 2.2 on 2020-02-03 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        # migrations.RemoveField(
        #     model_name='contact',
        #     name='nama',
        # ),
        # migrations.RemoveField(
        #     model_name='contact',
        #     name='nomer_hp',
        # ),
        # migrations.RemoveField(
        #     model_name='contact',
        #     name='slug',
        # ),
        # migrations.RemoveField(
        #     model_name='contact',
        #     name='tanggal_buat',
        # ),
        # migrations.AddField(
        #     model_name='contact',
        #     name='deskripsi',
        #     field=models.TextField(default=''),
        #     preserve_default=False,
        # ),
        # migrations.AddField(
        #     model_name='contact',
        #     name='facebook',
        #     field=models.CharField(default='', max_length=100),
        #     preserve_default=False,
        # ),
        # migrations.AddField(
        #     model_name='contact',
        #     name='instagram',
        #     field=models.CharField(default='', max_length=100),
        #     preserve_default=False,
        # ),
        # migrations.AddField(
        #     model_name='contact',
        #     name='moto',
        #     field=models.CharField(default='', max_length=100),
        #     preserve_default=False,
        # ),
        # migrations.AddField(
        #     model_name='contact',
        #     name='nomer_hp_dua',
        #     field=models.CharField(default='', max_length=20),
        #     preserve_default=False,
        # ),
        migrations.AddField(
            model_name='contact',
            name='nomer_hp_satu',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contact',
            name='alamat',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
