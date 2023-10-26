# Generated by Django 4.2.6 on 2023-10-26 12:50

import Petstagram23.photos.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0003_alter_photo_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=models.ImageField(blank=True, upload_to='mediafiles/pet_photos/', validators=[Petstagram23.photos.validators.validate_file_less_than_5mb]),
        ),
    ]
