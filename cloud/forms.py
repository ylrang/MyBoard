from django import forms
from .models import Post, Document

<<<<<<< HEAD
=======
from django.utils.translation import gettext_lazy as _

>>>>>>> 03f1c7b8136cbc7a9a3a3c078896f4af2ac3755f


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
<<<<<<< HEAD
        fields = ['title', 'content',  'author', 'category', 'institute']
=======
        fields = ['title', 'content', 'category', 'institute']
>>>>>>> 03f1c7b8136cbc7a9a3a3c078896f4af2ac3755f

class DocumentForm(forms.ModelForm):
    files = forms.FileField(label='첨부 파일', required=False, widget= forms.FileInput(attrs={'class': 'form'}))
    class Meta:
        model = Document
<<<<<<< HEAD
        exclude = ['attached', 'filename','content_type', 'size']
=======
        exclude = ['attached', 'filename', 'content_type', 'size']
>>>>>>> 03f1c7b8136cbc7a9a3a3c078896f4af2ac3755f
