from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.views.generic.detail import DetailView

from .models import Person
from django import forms
from django.db.models import fields

from weasyprint import HTML
import tempfile
from django.core.files.storage import FileSystemStorage
from django.template.loader import render_to_string
from django.http import  HttpResponse

#from .views2.attch_func_views import html_to_pdf_view
class PersonListView(ListView):
    model = Person
    queryset = Person.objects.all()

class PersonCreateView(CreateView):
    model = Person
    fields = '__all__'
    success_url = reverse_lazy('myia:list')


class PersonUpdateView(UpdateView):
    model = Person
    fields = '__all__'
    success_url = reverse_lazy('myia:list')


class PersonDetailView(DetailView):
    queryset = Person.objects.all()


class PersonDeleteView(DeleteView):
    queryset = Person.objects.all()
    success_url = reverse_lazy('myia:list')


class PdfView(ListView):
    model = Person
    queryset = Person.objects.all()

    def get(self, request):
            # Model data
        people = self.queryset

        # Rendered
        html_string = render_to_string('reports/pdf_template_from_views.html',
                {'people': people}
        )
        html = HTML(string=html_string)
        result = html.write_pdf()

        # Creating http response
        response = HttpResponse(content_type='application/pdf;')
        response['Content-Disposition'] = 'inline; filename=list_people.pdf'
        response['Content-Transfer-Encoding'] = 'binary'

        with tempfile.NamedTemporaryFile(delete=True) as output:
            output.write(result)
            output.flush()
            output = open(output.name, 'rb')
            response.write(output.read())

        return response