from django.db import models
import os
# Create your models here.
class BRNC(models.Model):
    SYSTEM_CHOICES = [
        ('1', '법률'),
        ('2', '규정'),
        ('3', '규제지침'),
    ]
    system = models.CharField(
        max_length=2,
        choices=SYSTEM_CHOICES
    )
    nation = models.CharField(max_length=10)
    doc_id = models.CharField(max_length=200)
    title = models.CharField(max_length=200, null=True, blank=True)
    file = models.FileField(upload_to='brnc/', null=True, blank=True)
    def __str__(self):
        return self.doc_id

    def get_filename(self):
        return os.path.basename(self.file.name)
    
    def get_content_type(self):
        return self.get_filename().split('.')[-1]
        

class Document(models.Model):
    brnc = models.ForeignKey(BRNC, on_delete=models.CASCADE, related_name='regulation_doc')
    institute = models.CharField(max_length=10)
    title = models.CharField(max_length=200)
    index = models.CharField(max_length=100)
    index_title = models.CharField(max_length=200)
    index_title_kr = models.CharField(max_length=200)
    index_content = models.TextField()
    index_content_kr = models.TextField()
    sector = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ('brnc__doc_id', 'title', 'index',)
    def __str__(self):
        return '{} {} {}'.format(self.brnc.doc_id, self.title, self.index_title_kr)
    
    def get_title(self):
        return '[{}] {}'.format(self.brnc.doc_id, self.title)
    
    def get_index_title(self):
        return '[{}] {}'.format(self.index, self.index_title)
    
    def get_index_title_kr(self):
        return '[{}] {}'.format(self.index, self.index_title_kr)

    
class UNIST(models.Model):
    DEVELOP_CHOICES = [
        ('1', '개념화'),
        ('2', '부지조사/선정'),
        ('3', '기준 설계/인허가 신청'),
        ('4', '건설'),
        ('5', '운영'),
        ('6', '폐쇄'),
    ]
    EVAL_CHOICES = [
        ('1', 'Safety Context'),
        ('2', '안전전략'),
        ('3', '부지 특성'),
        ('4', '처분장 설계'),
        ('5', '안전성 평가 방법론'),
        ('6', '운영 중 안전성 평가'),
        ('7', '폐쇄 후 안전성 평가'),
        ('8', '관리 시스템/이해관계자 및 규제기관 참여'),
        ('9', '증거들의 종합'),
        ('10', '불확실성 관리'),
        ('11', '한계점, 통제 및 조건'),
    ] 
    evaluation = models.CharField(
        max_length=20,
        choices=EVAL_CHOICES
    )
    eval1 = models.CharField(max_length=2, default='1')
    epg = models.BooleanField(default=False)
    develop = models.CharField(
        max_length=2,
        choices=DEVELOP_CHOICES
    )
    title = models.CharField(max_length=200)
    nation = models.CharField(max_length=10)
    background = models.TextField()
    regulation = models.TextField()
    image = models.ImageField(upload_to='unist/', null=True, blank=True)
    
    def __str__(self):
        return self.title


class Report(models.Model):
    title = models.CharField(max_length=200)
    institute = models.CharField(max_length=10)
    report_title = models.CharField(max_length=200)
    file = models.FileField(upload_to='unist/report/', null=True, blank=True)
    case_title = models.OneToOneField(UNIST, on_delete=models.CASCADE)
    def __str__(self):
        return self.report_title
    
    def get_filename(self):
        return os.path.basename(self.file.name)
    
    def get_content_type(self):
        return self.get_filename().split('.')[-1]
    
class Issue(models.Model):
    title = models.CharField(max_length=200)
    summary = models.TextField()
    proposal = models.TextField()
    category = models.CharField(max_length=100)
    report = models.ForeignKey(Report, related_name='issues', on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    
class Related(models.Model):
    report= models.ForeignKey(Report, on_delete=models.CASCADE, related_name='related_report')
    report_reviewed = models.CharField(max_length=200)
    section_reviewed = models.CharField(max_length=200)
    def __str__(self):
        return self.report.title