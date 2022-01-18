from django.forms import ModelForm
from myia.models import Person
from django import forms



class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'phone', 'andress', 'cpf']
