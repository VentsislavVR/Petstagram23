from django.core.validators import MinLengthValidator
from django.db import models

from Petstagram23.core.model_mixins import StrFromFieldsMixin
from Petstagram23.pets.models import Pet
from Petstagram23.photos.validators import validate_file_less_than_5mb


class Photo(StrFromFieldsMixin,models.Model):
    str_fields = ('pk','photo','location')

    MIN_DESCRIPTION_LENGTH = 30
    MAX_DESCRIPTION_LENGTH = 300

    MAX_LOCATION_LENGTH = 30

    photo = models.ImageField(
        upload_to='pet_photos/',
        # Requires mediafiles to work
        null=False,
        blank=True,
        validators=(validate_file_less_than_5mb,)
            )

    description = models.CharField(
            max_length=MAX_DESCRIPTION_LENGTH,
            validators=(
                MinLengthValidator(MIN_DESCRIPTION_LENGTH),
            ),
            null=True,
            blank=True
    )

    location = models.CharField(
        max_length=MAX_LOCATION_LENGTH,
        null=True,
        blank=True,

    )

    publication_date = models.DateField(
        auto_now_add=True,
        null=False,
        blank=True,
    )

    tagged_pets = models.ManyToManyField(
        Pet,
        blank=True,
    )