# Generated by Django 2.2 on 2020-02-17 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_contact_no_rekening'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='no_rekening',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
