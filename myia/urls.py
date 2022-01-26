#from django.contrib import admin
#from django.conf.urls import url
from django.urls import path

from myia import views 
#html_to_pdf_view
from .views import PdfView

app_name = 'myia'


urlpatterns = [ 

    #LIST
    path('', views.PersonListView.as_view(), name='list'),
    #CREATE
    path('create/', views.PersonCreateView.as_view(), name='create'),
    #UPDATE
    path('update/<int:pk>/', views.PersonUpdateView.as_view(), name='update'),
    #DETAIL
    path('detail/<int:pk>/', views.PersonDetailView.as_view(), name='detail'),
    #DELETE
    path('delete/<int:pk>/', views.PersonDeleteView.as_view(), name='delete'),
    #path('pdf/', views.PdfView.as_view(),name='pdf-data',),

    path('pdf/', PdfView.as_view(), name='pdf'),


    #PDF PRINT
    #path('pdf/', views.PdfView.as_view(), name='pdf'),   
    #path('html_to_pdf_view/',
    # Error Handling
#    path('error/', error, name='error'),
]
