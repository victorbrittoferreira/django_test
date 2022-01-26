from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from django.urls.conf import include

#from myia.views.person_views import (
#    views,
#    list_people,
#    create_person,
#    update_person,
#    delete_person,
#    )
#from myia.views.attch_func_views import error, html_to_pdf_view

#app_name = 'myia/views'

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', views.PersonListView.as_view(), name='/person_list'),

    path('myia/', include('myia.urls')), # better 
    #path('', include('myia.urls')),
]
#    #READ
#    path('', list_people, name='list_people'),
#    path('list', views.PersonList.as_view(), name='list_people'),
#    #CREATE
#    path('create_person/', create_person,
#        name = 'create_person'),
#    #UPDATE
#    path('update_person/<int:id>',
#        update_person, name = 'update_person'),
#    #DELETE
#    path('delete_person/<int:id>',
#        delete_person, name = 'delete_person'),
#    #PDF PRINT
#    path(r'html_to_pdf_view/',
#        html_to_pdf_view, name='html_to_pdf_view'),   
#    # Error Handling
#    path('error/', error, name='error'),
#]
