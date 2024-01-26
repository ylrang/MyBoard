from django.core.files.uploadedfile import SimpleUploadedFile
import unittest
from django.test import TestCase
from .models import *

# Create your tests here.
class MyTesetCase(unittest.TestCase):
    def setup(self):
        self.brnc = BRNC.objects.create(system='1', nation='국내', doc_id='a')

    def tearDown(self):
        BRNC.objects.all().delete()

    def test_system_create(self):
        brnc = BRNC.objects.create(system='1', nation='국내', doc_id='a')
        self.assertEqual(brnc.system, '1')
    
    def test_nation_create(self):
        brnc = BRNC.objects.create(system='1', nation='국내', doc_id='a')
        self.assertEqual(brnc.nation, '국내')
    
    def test_doc_id_create(self):
        brnc = BRNC.objects.create(system='1', nation='국내', doc_id='a')
        self.assertEqual(brnc.nation, 'a')
        
    def test_title_create(self):
        brnc = BRNC.objects.create(system='1', nation='국내', doc_id='a', title='제목')
        self.assertEqual(brnc.title, '제목')
    
    def test_file_create(self):
        uploaded_file = SimpleUploadedFile('file.txt', b'file_content', content_type='application/octet-stream')
        brnc = BRNC.objects.create(system='1', nation='국내', doc_id='a', file=uploaded_file)
        self.assertIsInstance(uploaded_file, brnc)
        self.assertEqual(brnc.filename, 'file.txt')
