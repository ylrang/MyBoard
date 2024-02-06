from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from .models import *
from .forms import CaseForm
from django.http import FileResponse
from django.core.files.storage import FileSystemStorage
from django.utils import timezone

# Create your views here.
class about(TemplateView):
    template_name = "rnd/about.html"
        
class case(TemplateView):
    template_name = "rnd/process_case.html"
    
def create_case(request):
    if request.method == 'POST':
        form = CaseForm(request.POST, request.FILES)
        if form.is_valid():
            case = form.save(commit=False)
            if 'save' in request.POST:
                case.published = timezone.now()
                case.updated = timezone.now()
            case.save()
            return redirect('rnd:case_detail', pk=case.pk)
    else:
        form = CaseForm()
    return render(request, 'rnd/contact.html', {'form': form})

def modify_case(request, pk):
    case = get_object_or_404(Case, pk=pk)
    if request.method == 'POST':
        form = CaseForm(request.POST, request.FILES, instance=case)
        if form.is_valid():
            case = form.save(commit=False)
            case.updated = timezone.now()
            case.save()
            return redirect('rnd:case_detail', pk=case.pk)
    else:
        form = CaseForm(instance=case)
    return render(request, 'rnd/contact.html', {'form': form})

def case_draft_list(request):
    cases = Case.objects.filter(published__isnull=True).order_by('created')
    return render(request, 'rnd/case_list.html', {'cases': cases})

def publish_case(request, pk):
    case = get_object_or_404(Case, pk=pk)
    case.publish()
    return redirect('case_detail', pk=pk)

def KAERI_cases(request):
    cases = Case.objects.filter(institute='1').filter(published__isnull=False).order_by('created')
    return render(request, 'rnd/case_list.html', {'cases': cases})

def KOLAD_cases(request):
    cases = Case.objects.filter(institute='2').filter(published__isnull=False).order_by('created')
    return render(request, 'rnd/case_list.html', {'cases': cases})

def case_detail(request, pk):
    case = Case.objects.get(pk=pk)
    comments = Comment.objects.filter(case=case)
    return render(request, 'rnd/single-blog.html', {'case': case, 'comments': comments})

def download_file(request, pk):
    case = Case.objects.get(pk=pk)
    file_path = case.file.path
    fs = FileSystemStorage(file_path)
    response = FileResponse(fs.open(case.file, 'rb'), content_type='application/force-download')
    response['Content-Disposition'] = f'attachment; filename="{case.file.name}"'
    return response