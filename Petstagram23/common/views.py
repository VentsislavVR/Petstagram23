import pyperclip
from django.shortcuts import render, redirect, resolve_url
from django.urls import reverse
from pyperclip import copy

from Petstagram23.common.models import PhotoLike
from Petstagram23.common.utils import get_user_liked_photos, get_photo_url
from Petstagram23.core.photo_utils import apply_likes_count, apply_user_liked_photo
from Petstagram23.photos.models import Photo


# Create your views here.

def index(request):
    photos = [apply_likes_count(photo) for photo in Photo.objects.all()]
    photos = [apply_user_liked_photo(photo) for photo in photos]

    context = {
        'photos': photos
    }
    return render(request,
                  'common/home-page.html',
                  context, )





def like_photo(request, photo_id):
    user_liked_photos = get_user_liked_photos(photo_id)

    if user_liked_photos:
        user_liked_photos.delete()

    else:
        PhotoLike.objects.create(
            photo_id=photo_id)
    redirect_path = request.META['HTTP_REFERER'] + f'#photo-{photo_id}'
    return redirect(get_photo_url(request,photo_id))

def share_photo(request,photo_id):
    photo_details_url =\
        reverse('details photo',
                kwargs={'pk':photo_id
    })

    pyperclip.copy(photo_details_url)
    return redirect(get_photo_url(request,photo_id))

