from django.contrib import admin
from django.conf.urls import url
from django.urls import path

from myia.views import (
    list_people,
    create_person,
    update_person,
    delete_person,
    error,
    html_to_pdf_view
    )

urlpatterns = [
    path('admin/', admin.site.urls),
 
    #READ
    path('', list_people, name='list_people'),
    #CREATE
    path('create_person/', create_person,
        name = 'create_person'),
    #UPDATE
    path('update_person/<int:id>',
        update_person, name = 'update_person'),
    #DELETE
    path('delete_person/<int:id>',
        delete_person, name = 'delete_person'),
    #PDF PRINT
    path(r'html_to_pdf_view/',
        html_to_pdf_view, name='html_to_pdf_view'),   
    # Error Handling
    path('error/', error, name='error'),
]
