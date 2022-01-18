from .forms.form_person import PersonForm  
from .models import Person

from django.shortcuts import render, redirect, reverse
from django.http import  HttpResponse

from django.core.files.storage import FileSystemStorage
from django.template.loader import render_to_string

from weasyprint import HTML
import tempfile


def create_person(request):
    try:
        form = PersonForm(request.POST or None)

        if form.is_valid():
            form.save()

            return redirect('list_people')

        return render(request, 
            'create_person_form.html', {'form': form})

    except:
        return redirect(reverse('error'))
    
def list_people(request):
    people = Person.objects.all()
    return render(request, 
        'list_people.html', {'people': people})

def update_person(request,id):
    person = Person.objects.get(id=id)
    form = PersonForm(request.POST or None, instance=person)

    if form.is_valid():
        form.save()
        return redirect('list_people')

    return render(request, 'create_person_form.html',
        {'form': form, 'person': person})

def delete_person(request, id):
    try:
        person = Person.objects.get(id=id)

        if request.method == 'POST':
            person.delete()
            return redirect('list_people')

        return render(request, 
            'delete_person_confirm.html', {'person': person})

    except:
        return redirect(reverse('error'))

def error(request):
    return render(request, "error.html",)

def html_to_pdf_view(request):
    """Generate pdf."""

    # Model data
    people = Person.objects.all().order_by('id')

    # Rendered
    html_string = render_to_string(
        'reports/pdf_template_from_views.html',{'people': people})
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