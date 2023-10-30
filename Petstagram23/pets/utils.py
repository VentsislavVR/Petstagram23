from Petstagram23.pets.models import Pet


# def get_pet_by_name_and_username(pet_slug,username):
#
#     return Pet.objects.get(name=pet_slug)
def get_pet_by_name_and_username(pet_slug, username):
    return Pet.objects \
        .filter(slug=pet_slug) \
        .get()
#TODO fix username when auth