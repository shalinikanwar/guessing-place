# Generated by Django 4.2.3 on 2023-09-14 02:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_profile_id_alter_profile_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='image',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='location',
        ),
    ]
