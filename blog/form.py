from django import forms
from .models import Post


class CodeForm(forms.Form):
    code = forms.CharField(label='code',max_length=12)
