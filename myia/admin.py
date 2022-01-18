from django.contrib import admin
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.template.loader import render_to_string

from weasyprint import HTML
from django_object_actions import DjangoObjectActions

from .models import Person
from .forms.form_person import PersonFormAdmin

#@admin.register(Person)
class PersonAdmin(DjangoObjectActions, admin.ModelAdmin):
        #fields = ['name', 'phone', 'andress', 'cpf']
        list_display = ['name', 'phone', 'andress', 'cpf']
        search_fields = ['name', 'phone', 'andress', 'cpf']

        form = PersonFormAdmin
        class Media: 
                js=(
                        "jquery.mask.min.js",
                        "jquery-3.6.0.min.js", 
                        "mask.js",
                )


        def generate_pdf(self, request, obj):
                html_string = render_to_string('reports/pdf_template.html',
                        {'obj': obj}
                )

                html = HTML(string=html_string)
                html.write_pdf(target='/tmp/{}.pdf'.format(obj));

                fs = FileSystemStorage('/tmp')
                with fs.open('{}.pdf'.format(obj)) as pdf:
                        response = HttpResponse(pdf, 
                                content_type='application/pdf')
                        response['Content-Disposition'] = 'attachment; filename="{}.pdf"'.format(obj)
                        return response

                return response

        generate_pdf.label = 'Gerar PDF'

        change_actions = ('generate_pdf',)



admin.site.register(Person, PersonAdmin)
        
