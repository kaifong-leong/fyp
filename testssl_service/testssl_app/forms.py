from django import forms
from .models import URLItem

class URLForm(forms.ModelForm):
    class Meta:
        model = URLItem
        fields = "__all__"