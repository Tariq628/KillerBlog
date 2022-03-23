from cProfile import label
from enum import auto
from django import forms
from blog.models import Contact
from ckeditor.widgets import CKEditorWidget
class ContactFrom(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget(attrs={'placeholder':"Type.."}))
    class Meta:
        model = Contact
        fields = ['content']