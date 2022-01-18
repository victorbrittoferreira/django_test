from django.contrib import admin
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.template.loader import render_to_string

from .models import Person


from weasyprint import HTML
from django_object_actions import DjangoObjectActions

@admin.register(Person)
class PersonAdmin(DjangoObjectActions, admin.ModelAdmin):
        fields = ['id','name', 'phone', 'andress', 'cpf']
        list_display = ['id','name', 'phone_mask', 'andress', 'cpf']
        search_fields = ['id','name', 'phone', 'andress', 'cpf']



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
        #generate_pdf.short_description = 'Clique para gerar o PDF dessa ordem de serviço'

        change_actions = ('generate_pdf',)


        
