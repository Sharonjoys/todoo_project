from django import forms
from .models import task



class newmodelform(forms.ModelForm):
    class Meta:
        model=task
        fields=['name','priority','date']