from myia.models import Person
from myia.forms.person import PersonForm  

from django.shortcuts import render, redirect, reverse



def add_person(request):
    pass
    
def list_details_person(request, id):
    pass

def delete_person(request, id):
    pass

def error(request):
    context = {
    }
    return render(request, "myia/error.html", context)
