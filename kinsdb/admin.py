from django.contrib import admin
from .models import *

# Register your models here.
class DocumentAdmin(admin.ModelAdmin):
    model = Document
    list_display=['brnc','title','index',]

admin.site.register(BRNC)
admin.site.register(Document, DocumentAdmin)
admin.site.register(UNIST)
admin.site.register(Report)
admin.site.register(Issue)
admin.site.register(Related)