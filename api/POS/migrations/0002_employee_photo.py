# Generated by Django 3.1.6 on 2021-02-16 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('POS', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
