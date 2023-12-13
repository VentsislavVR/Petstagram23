from django.contrib.auth import get_user_model
from django.db import models

from Petstagram23.photos.models import Photo

UserModel = get_user_model()
# Create your models here.


class PhotoComment(models.Model):
    MAX_TEXT_LENGTH = 300
    text = models.CharField(
        max_length=MAX_TEXT_LENGTH,
        null=False,
        blank=False

    )
    publication_date_and_time = models.DateField(
        auto_now_add=True,
        blank=True,
        null=False,
    )
    photo = models.ForeignKey(
        Photo,
        on_delete=models.RESTRICT,
        null=False,
        blank=True,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.DO_NOTHING,

    )



class PhotoLike(models.Model):
    photo = models.ForeignKey(
        Photo,
        on_delete=models.RESTRICT,
        null=False,
        blank=True,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.DO_NOTHING,
    )
