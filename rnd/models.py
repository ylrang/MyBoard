from django.db import models
from django.utils import timezone

# Create your models here.
class Case(models.Model):
    INST_CHOICES = [
        ('1', 'KAERI'),
        ('2', 'KORAD'),
    ]
    title = models.CharField(default='1차 보고서', max_length=100)
    institute = models.CharField(
        max_length=2,
        choices=INST_CHOICES,
    )
    content = models.TextField(blank=True)
    file = models.FileField(upload_to='rnd/', null=True, blank=True)
    PIC = models.CharField(default='홍길동', max_length=100)
    created = models.DateTimeField(default=timezone.now)
    published = models.DateTimeField(blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)
    inprocess = models.BooleanField(default=True)
    
    def publish(self):
        self.published = timezone.now()
        self.updated = timezone.now()
        self.save()
    
    def __str__(self):
        return self.title