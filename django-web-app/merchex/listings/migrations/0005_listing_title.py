# Generated by Django 4.2.2 on 2023-06-16 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0004_listing_delete_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='title',
            field=models.CharField(default='item', max_length=100),
        ),
    ]
