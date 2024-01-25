from django.test import TestCase
from .models import *
# Create your tests here.
class CaseModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Case.objects.create(institute='1')
    
    def test_title_label(self):
        case = Case.objects.get(id=1)
        field_label = case._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'title')
    
    def test_institute_label(self):
        case = Case.objects.get(id=1)
        field_label = case._meta.get_field('institute').verbose_name
        self.assertEquals(field_label, 'institute')

    def test_content_label(self):
        case = Case.objects.get(id=1)
        field_label = case._meta.get_field('content').verbose_name
        self.assertEquals(field_label, 'content')

    def test_file_label(self):
        case = Case.objects.get(id=1)
        field_label = case._meta.get_field('file').verbose_name
        self.assertEquals(field_label, 'file')

    def test_PIC_label(self):
        case = Case.objects.get(id=1)
        field_label = case._meta.get_field('PIC').verbose_name
        self.assertEquals(field_label, 'PIC')

    def test_created_label(self):
        case = Case.objects.get(id=1)
        field_label = case._meta.get_field('created').verbose_name
        self.assertEquals(field_label, 'created')

    def test_published_label(self):
        case = Case.objects.get(id=1)
        field_label = case._meta.get_field('published').verbose_name
        self.assertEquals(field_label, 'published')

    def test_updated_label(self):
        case = Case.objects.get(id=1)
        field_label = case._meta.get_field('updated').verbose_name
        self.assertEquals(field_label, 'updated')

    def test_inprocess_label(self):
        case = Case.objects.get(id=1)
        field_label = case._meta.get_field('inprocess').verbose_name
        self.assertEquals(field_label, 'inprocess')
        