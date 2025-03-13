from django import forms
from .models import URLItem, TestsslScan

class URLForm(forms.ModelForm):
    class Meta:
        model = URLItem
        # fields = "__all__"
        fields = ['url']

class TestsslForm(forms.ModelForm):
    class Meta:
        model = TestsslScan
        fields = ['url']