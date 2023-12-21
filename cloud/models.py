from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
<<<<<<< HEAD
from django.urls import reverse
=======
>>>>>>> 03f1c7b8136cbc7a9a3a3c078896f4af2ac3755f
import os
# Create your models here.
class Post(models.Model):
    INSTITUTE_CHOICES = [
        ('1', 'KINS'),
        ('2', 'NCS'),
        ('3', 'UNIST'),
        ('4', 'BRNC'),
    ]
    CATEGORY_CHOICES = [
        ('1', 'N/Star'),
        ('2', '논문'),
        ('3', '보고서'),
        ('4', '일정'),
    ]
    #author = models.ForeignKey(User, on_delete=models.CASCADE)
    author = models.CharField(max_length=10, default='admin')
    institute = models.CharField(
        max_length=2,
        choices=INSTITUTE_CHOICES,
    )
    title = models.CharField(max_length=200)
    category = models.CharField(
        max_length=2,
        choices=CATEGORY_CHOICES,
    )
    content = models.TextField()
    #document = models.FileField(upload_to='', null=True, blank=True)
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
<<<<<<< HEAD
    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})





def get_file_path(instance, filename):
    return 'user_{}/{}'.format(instance.id, filename)

class Document(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='files', verbose_name='Post', blank=True, null=True)
    attached = models.FileField(upload_to=get_file_path, null=True, blank=True, verbose_name='file')
=======
    """def get_filename(self):
        return os.path.basename(self.document.name)
    
    def get_filetype(self):
        return self.get_filename().split('.')[-1]
    
    def delete(self, *args, **kargs):
        if self.document:
            os.remove(os.path.join(settings.MEDIA_ROOT, self.document.path))
        super(Post, self).delete(*args, **kargs)"""

class Document(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='files', verbose_name='Post', blank=True, null=True)
    attached = models.FileField(upload_to='', null=True, blank=True, verbose_name='file')
>>>>>>> 03f1c7b8136cbc7a9a3a3c078896f4af2ac3755f
    filename = models.CharField(max_length=64, null=True, verbose_name='filename')
    content_type = models.CharField(max_length=128, null=True, verbose_name='MIME TYPE')
    size = models.IntegerField('file size', null=True)
    
    def __str__(self):
<<<<<<< HEAD
        return self.filename
    
    def save(self, *args, **kwargs):
        if self.id is None:
            temp_file = self.attached
            self.attached = None
            super().save(*args, **kwargs)
            self.attached = temp_file
        super().save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        if self.attached:
            os.remove(os.path.join(settings.MEDIA_ROOT, self.attached.path))
        super().delete(*args, **kwargs)
=======
        return self.filename
>>>>>>> 03f1c7b8136cbc7a9a3a3c078896f4af2ac3755f
