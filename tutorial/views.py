from pyramid.view import view_config
from pyramid.response import Response, FileResponse
from pyramid.renderers import render
import pdfkit
import pdb

from io import StringIO


#First view, available att http://localhost:6543
@view_config(route_name='home', renderer='home.jinja2')
def home(request):
    #pdb.set_trace()
    return {'name': 'Home View'}


# /howdy
@view_config(route_name='hello', renderer='home.jinja2')
def hello(request):
    return {'name': 'Hello View'}


@view_config(route_name='pdftest', renderer='pdftest.jinja2')
def pdftest(request):
    return {'name': 'pdftest'}

@view_config(route_name='pdfform', renderer='pdftest.jinja2')
def pdfform(request):
    #pdb.set_trace()
    return {}

@view_config(route_name='create_pdf')
def create_pdf(request):
    session = request.session
    #pdf = pdfkit.from_url('www.wikipedia.org', '/pdfnew/foo.pdf')
    #return {'name': 'Anger rising', 'pdf': '/pdfnew/foo.pdf'}
    if 'name' in request.GET:
        result = str(render('tutorial:pdfgen.jinja2', {'name': request.GET['foo']}, request=request))
        session['name']=request.GET['foo']
        request.session['name'] = session['name']
    else:
        result = str(render('tutorial:pdftest.jinja2', {}, request=request))
        session['name']='nofoo'
        request.session['name'] = session['name']
    print(result);

    pdffileio = StringIO()
    pdffileio.write(result)
    pdf_as_string = pdfkit.from_string(result, False)

    response = Response(
    pdf_as_string,

    content_disposition="attachment; filename={}.pdf".format(request.pdtb_id),
    content_type = "application/pdf",
    charset="utf-8"
    )

    return response
