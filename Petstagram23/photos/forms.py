from django import forms

from Petstagram23.common.models import PhotoLike, PhotoComment
from Petstagram23.core.form_mixins import DisabledFormMixin
from Petstagram23.photos.models import Photo


class PhotoBaseForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('photo', 'description', 'location', 'tagged_pets')


class PhotoCreateForm(PhotoBaseForm):
   ...


class PhotoEditForm(PhotoBaseForm):
    class Meta:
        model = Photo
        fields = ('description', 'location', 'tagged_pets')
        exclude = ('photo',)


class PhotoDeleteForm(DisabledFormMixin, PhotoBaseForm):
    disabled_fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._disable_fields()

    def save(self, commit=True):
        if commit:
            self.instance.tagged_pets.clear()  # many to many
            PhotoLike.objects.filter(photo_id=self.instance.id) \
                .delete()  # one to many
            PhotoComment.objects.filter(photo_id=self.instance.id) \
                .delete()  # one to many
            # self.instance.save()
            self.instance.delete()
        return self.instance
