#from django.forms import ModelForm

from django import forms
from .models import Person

class PersonForm(forms.ModelForm):

    class Meta:
        model = Person
        fields = '__all__'
    
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['phone'].widget.attrs.update({'class': 'mask-phone'})
        self.fields['cpf'].widget.attrs.update({'class': 'mask-cpf'})



