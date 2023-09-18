# Generated by Django 4.2.3 on 2023-09-15 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_remove_profile_image_remove_profile_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='age',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='place',
            field=models.CharField(default='', max_length=100),
        ),
    ]