# Generated by Django 4.2.6 on 2023-12-03 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FindMyFurryFriend', '0007_lostpet_agree_to_share_location_lostpet_latitude_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='foundpet',
            name='agree_to_share_location',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='foundpet',
            name='latitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='foundpet',
            name='longitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='foundpet',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='lost_pets/'),
        ),
    ]