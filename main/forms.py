from .models import Request
from django import forms

class RequestForm(forms.ModelForm):
    name = forms.CharField(max_length=255)
    phone = forms.CharField(max_length=255)

    class Meta:
        model = Request
        fields = ('name','phone')
