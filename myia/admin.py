from django.contrib import admin
from myia import models

@admin.register(models.Person)
class PersonAdmin(admin.ModelAdmin):
        fields = ['name', 'phone', 'andress', 'cpf']
        list_display = ['name', 'phone_mask', 'andress', 'cpf']
        search_fields = ['name', 'phone', 'andress', 'cpf']
        
