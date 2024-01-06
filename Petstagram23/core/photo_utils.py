
def apply_likes_count(photo):
    photo.likes_count = photo.photolike_set.count()
    return photo


def apply_user_liked_photo(photo,user):

    photo.is_liked_by_user = user.is_authenticated and user in photo.photolike_set.all()
    return photo

