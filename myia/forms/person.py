from django.forms import ModelForm
#from input_mask.widgets import InputMask
from myia.models import Person
from django import forms



class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'phone', 'andress', 'cpf']
