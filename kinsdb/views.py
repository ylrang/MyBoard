from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from .models import *
from django.http import FileResponse
from django.core.files.storage import FileSystemStorage

# Create your views here.
class index(TemplateView):
    template_name = "kinsdb/database.html"

def brnc(request):
    brnc_list = BRNC.objects.all()
    return render(request, 'kinsdb/brnc_db.html', {'brnc_list': brnc_list})

def regulation_list(request):
    kw = request.GET.get('kw', '')
    doc_id = request.GET.get('doc_id', '문서')
    sector = request.GET.get('sector', '부문')
    form = {
        'kw': kw,
        'doc_id': doc_id,
        'sector': sector,
    }
    id_list = BRNC.objects.values_list('doc_id', flat=True).distinct()
    sector_list = Document.objects.values_list('sector', flat=True).order_by('-sector').distinct()
    ids = [(i, id_list[i]) for i in range(len(id_list))]
    sectors = [(i, sector_list[i]) for i in range(len(sector_list))]
    choices = {
        'ids': ids,
        'sectors' : sectors,
    }
    filter_args={}
    if kw != '':
        filter_args['title__icontains'] = kw
    if doc_id != '문서':
        filter_args['brnc__doc_id'] = doc_id
    if sector != '부문':
        filter_args['sector'] = sector
    query = Document.objects.filter(**filter_args)
    return render(request, 'kinsdb/regulation_docs.html', {**form, **choices, 'documents': query})

def doc_details(request, pk):
    document = Document.objects.get(pk=pk)
    return render(request, 'kinsdb/doc_details.html', {'document': document})

def unist(request):
    objects = UNIST.objects.all()
    choices = {
        'd_choices': UNIST.DEVELOP_CHOICES,
        'e_choices' : UNIST.EVAL_CHOICES,
        'epg_choices' : ['True', 'False'],
    }
    return render(request, 'kinsdb/unist_db.html', {'unist_list': objects, **choices})

def report_details(request, pk):
    report = Report.objects.get(case_title=pk)
    return render(request, 'kinsdb/regulation_report.html', {'report': report})

def issue_details(request, pk):
    issue = Issue.objects.get(pk=pk)
    return render(request, 'kinsdb/issue_details.html', {'issue': issue})

def download_file(request, pk):
    object = BRNC.objects.get(pk=pk)
    file_path = object.file.path
    file_name = object.get_filename()
    fs = FileSystemStorage(file_path)
    response = FileResponse(fs.open(file_path, 'rb'), content_type='application/vnd.hancom.hwp')
    response['Content-Disposition'] = f'attachment; filename={file_name}'
    
    return response