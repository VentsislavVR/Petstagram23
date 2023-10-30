from django import forms

from Petstagram23.pets.models import Pet


class PetCreateForm(forms.ModelForm):
    # def __init__(self,*args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['name'].widget.attrs['placeholder'] = 'Pet name'
    #
    class Meta:
        model = Pet
        # fields = '__all__'
        fields = ('name', 'date_of_birth','personal_photo')
        # exclude = ('slug',)
        labels = {
            'name':'Pet Name',
            'personal_photo':'Link to Image',
            'date_of_birth':'Date of Birth',
        }

        widgets = {
        'name':forms.TextInput(
            attrs={
                'placeholder':'Pet name',
            }
        ),
            'date_of_birth':forms.DateInput(
            attrs={
                'placeholder':'mm/dd/yyyy',
                'type':'date',
            }
            ),
            'personal_photo':forms.URLInput(
                attrs={
                    'placeholder':'Link to image',
                }
            )
        }
class PetEditForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = '__all__'

class PetDeleteForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = '__all__'