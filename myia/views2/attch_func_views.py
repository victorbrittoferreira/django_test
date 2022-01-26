#
#
#from models2 import person_models
#from django.shortcuts import render, redirect, reverse
#
#from django.core.files.storage import FileSystemStorage
#from django.template.loader import render_to_string
#from django.http import  HttpResponse
#
#from weasyprint import HTML
#import tempfile
#
#
#def html_to_pdf_view(request):
#    """Generate pdf."""
#
#    # Model data
#    people = Person.objects.all().order_by('id')
#
#    # Rendered
#    html_string = render_to_string('reports/pdf_template_from_views.html',{'people': people})
#    html = HTML(string=html_string)
#    result = html.write_pdf()
#
#    # Creating http response
#    response = HttpResponse(content_type='application/pdf;')
#    response['Content-Disposition'] = 'inline; filename=list_people.pdf'
#    response['Content-Transfer-Encoding'] = 'binary'
#
#    with tempfile.NamedTemporaryFile(delete=True) as output:
#        output.write(result)
#        output.flush()
#        output = open(output.name, 'rb')
#        response.write(output.read())
#
#    return response



#def error(request):
#    return render(request, "error.html",)