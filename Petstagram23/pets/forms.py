from django import forms

from Petstagram23.core.form_mixins import DisabledFormMixin
from Petstagram23.pets.models import Pet


class PetBaseForm(forms.ModelForm):
    class Meta:
        model = Pet
        # fields = '__all__'
        fields = ('name', 'date_oof_birth', 'personal_photo')
        # exclude = ('slug',)
        labels = {
            'name': 'Pet Name',
            'personal_photo': 'Link to Image',
            'date_oof_birth': 'Date of Birth',
        }

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Pet name',
                }
            ),
            'date_oof_birth': forms.DateInput(
                attrs={
                    'placeholder': 'mm/dd/yyyy',
                    'type': 'date',
                }
            ),
            'personal_photo': forms.URLInput(
                attrs={
                    'placeholder': 'Link to image',
                }
            )
        }


class PetCreateForm(PetBaseForm):
    # def __init__(self,*args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['name'].widget.attrs['placeholder'] = 'Pet name'
    ...


class PetEditForm(PetBaseForm):
    ...


class PetDeleteForm(DisabledFormMixin, PetBaseForm):
    disabled_fields = ('name', 'date_oof_birth', 'personal_photo')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._disable_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        else:
            pass
        return self.instance
