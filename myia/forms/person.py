from django.forms import ModelForm
#from input_mask.widgets import InputMask
from models import Person
from django import forms



class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'phone', 'andress', 'cpf']
