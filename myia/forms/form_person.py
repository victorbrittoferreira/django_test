from django.forms import ModelForm
from myia.models import Person
from django import forms

from django.forms import ModelForm
from myia.models import Person
from django import forms

class PersonFormAdmin(forms.ModelForm):
    def __init__(self,*args, **kwargs):
        super(PersonFormAdmin, self).__init__(*args, **kwargs)
        self.fields['phone'].widget.attrs.update({'class': 'mask-phone'})
        self.fields['cpf'].widget.attrs.update({'class': 'mask-cpf'})

class PersonForm(forms.ModelForm):

    class Meta:
        model = Person
        #fields = ['name', 'phone', 'andress', 'cpf']
        fields = '__all__'
    
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['phone'].widget.attrs.update({'class': 'mask-phone'})
        self.fields['cpf'].widget.attrs.update({'class': 'mask-cpf'})


        


