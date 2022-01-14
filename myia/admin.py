from django.contrib import admin
from myia import models

# Register your models here.
@admin.register(models.Person)
class PersonAdmin(admin.ModelAdmin):
        fields = ['name', 'phone', 'andress', 'cpf']
