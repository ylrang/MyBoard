from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.db.models import Q
from django.urls import reverse, reverse_lazy
from .models import Post, Document
from .forms import PostForm, DocumentForm
from django.core.paginator import Paginator
from django.forms import modelformset_factory
from django.views.generic import CreateView, UpdateView, DeleteView

# Create your views here.
"""def index(request):
    posts = Post.objects.all()
    return render(request, 'cloud/jobs.html', {'posts': posts})
"""
def index(request):
    type = request.GET.get('type', '1')
    kw = request.GET.get('kw', '')
    inst = request.GET.get('institute', '0')
    cat = request.GET.get('category', '0')
    sort = request.GET.get('sort', '1')
    if sort == '1':
        posts = Post.objects.order_by('-created')
    elif sort == '2':
        posts = Post.objects.order_by('created')
    if kw:
        if type == '1':
            posts = posts.filter(Q(title__icontains=kw)).distinct()
        elif type == '2':
            posts = posts.filter(Q(content__icontains=kw)).distinct()
        elif type == '3':
            posts = posts.filter(Q(title__content__icontains=kw)).distinct()
        elif type == '4':
            posts = posts.filter(Q(author__icontains=kw)).distinct()
    if inst == '0':
        posts = posts
    else:
        posts = posts.filter(institute=inst)
    if cat == '0':
        posts = posts
    else:
        posts = posts.filter(category=cat)
    
    page = request.GET.get('page', '1')
    paginator = Paginator(posts, 6)
    page_obj = paginator.get_page(page)
    
    return render(request, 'cloud/jobs.html', {'posts': page_obj})

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'cloud/job_details.html', {'post' : post})


class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content', 'author', 'category', 'institute']
    success_url = reverse_lazy('index')
    template_name = 'cloud/job_form.html'

    def form_valid(self, form):
        form.instance.created = timezone.now()
        response = super().form_valid(form)

        for file in self.request.FILES.getlist('files'):
            if file:
                upload = Document(post=self.object, attached=file, filename=file.name, content_type=file.content_type, size=file.size)
                upload.save()
        return response

class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'content', 'category', 'institute']
    template_name = 'cloud/job_form.html'
    success_url = reverse_lazy('detail')
    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.object.pk})
    
    def form_valid(self, form):
        form.instance.updated = timezone.now()
        response = super().form_valid(form)

        for file in self.request.FILES.getlist('files'):
            if file:
                upload = Document(post=self.object, attached=file, filename=file.name, content_type=file.content_type, size=file.size)
                upload.save()
        return response


def delete_post(request, pk):
    post = Post.objects.get(pk=pk)
    files = Document.objects.filter(post=post)
    post.delete()
    for file in files:
        file.delete()
    return redirect('index')

from django.http import FileResponse
from django.core.files.storage import FileSystemStorage

def download_file(request, pk):
    file = Document.objects.get(pk=pk)
    file_path = file.attached.path
    fs = FileSystemStorage(file_path)
    response = FileResponse(fs.open(file_path, 'rb'), content_type=file.content_type)
    response['Content-Disposition'] = f'attachement; filename={file.filename}'
    
    return response

