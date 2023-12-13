# Generated by Django 4.2.6 on 2023-12-13 21:58

import Petstagram23.accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_petstagramuser_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='petstagramuser',
            name='gender',
            field=models.CharField(choices=[('male', 'MALE'), ('female', 'FEMALE'), ('d0 not show', 'DO_NOT_SHOW')], default=Petstagram23.accounts.models.Gender['DO_NOT_SHOW'], max_length=11),
        ),
    ]