# Generated by Django 4.0.6 on 2022-11-30 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='variation',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
