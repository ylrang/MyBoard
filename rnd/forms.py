from django import forms
from .models import Case

class CaseForm(forms.ModelForm):
    institute = forms.ChoiceField(choices=Case.INST_CHOICES, required=True)
    class Meta:
        model = Case
        fields = ['institute', 'content', 'file', 'PIC',]