import pyperclip
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse


from Petstagram23.common.forms import PhotoCommentForm, SearchPhotoForm
from Petstagram23.common.models import PhotoLike
from Petstagram23.common.utils import get_photo_url

from Petstagram23.core.photo_utils import apply_likes_count, apply_user_liked_photo
from Petstagram23.photos.models import Photo


# Create your views here.

def index(request):
    search_form = SearchPhotoForm(request.GET)
    search_pattern = None
    if search_form.is_valid():
        search_pattern = search_form.cleaned_data['pet_name']

    photos = Photo.objects.all()
    if search_pattern:
        photos = photos.filter(tagged_pets__name__icontains=search_pattern)
    user = request.user
    photos = [apply_likes_count(photo) for photo in photos]
    photos = [apply_user_liked_photo(photo,user) for photo in photos]

    context = {
        'photos': photos,
        'comment_form': PhotoCommentForm(),
        'search_form': search_form,
    }
    return render(request,
                  'common/home-page.html',
                  context, )

@login_required
def like_photo(request, photo_id):
    photo = Photo.objects.get(pk=photo_id)

    kwargs = {
        'photo': photo,
        'user': request.user }

    like_object = (PhotoLike.objects
                   .filter(**kwargs)
                   .first())
    # user_liked_photos = get_user_liked_photos(photo_id)

    if like_object:
        like_object.delete()
    else:
        new_like_obj = PhotoLike(**kwargs)
        new_like_obj.save()

    # redirect_path = request.META['HTTP_REFERER'] + f'#photo-{photo_id}'
    return redirect(get_photo_url(request, photo_id))

@login_required
def share_photo(request, photo_id):
    photo_details_url = \
        reverse('details photo',
                kwargs={'pk': photo_id
                        })

    pyperclip.copy(photo_details_url)
    return redirect(get_photo_url(request, photo_id))

@login_required
def comment_photo(request, photo_id):
    photo = Photo.objects.filter(pk=photo_id).get()

    form = PhotoCommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.photo = photo
        comment.save()

    return redirect('index')
