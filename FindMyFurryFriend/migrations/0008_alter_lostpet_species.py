# Generated by Django 4.2.5 on 2023-12-05 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FindMyFurryFriend', '0007_foundpet_agree_to_share_location_foundpet_latitude_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lostpet',
            name='species',
            field=models.CharField(max_length=50, verbose_name='Animal Species'),
        ),
    ]