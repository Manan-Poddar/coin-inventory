# Generated by Django 4.0.1 on 2024-07-06 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycoinApp', '0004_coinstatecondition_back_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coinstatecondition',
            name='back_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/coins/coin1.jpg'),
        ),
        migrations.AlterField(
            model_name='coinstatecondition',
            name='front_image',
            field=models.ImageField(blank=True, default='images/coins', null=True, upload_to='images/coins'),
        ),
    ]
