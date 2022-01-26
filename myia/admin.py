from django.contrib import admin
#from .models.person_models import Person
from .models import Person

#from .forms.person_form import PersonForm
from .forms import PersonForm

#@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
#class PersonAdmin(admin.ModelAdmin):
        list_display = ['name', 'phone', 'andress', 'cpf']
        search_fields = ['name', 'phone', 'andress', 'cpf']

        form = PersonForm
        class Media: 
                js=(
                        "js/jquery.mask.min.js",
                        "js/jquery-3.6.0.min.js", 
                        "js/mask.js",
                )


admin.site.register(Person, PersonAdmin)