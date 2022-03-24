from cProfile import label
from enum import auto
from django import forms
from blog.models import Contact
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget
class ContactFrom(forms.ModelForm):
    # content = forms.CharField(widget=CKEditorWidget(attrs={'placeholder':"Type.."}))
    # content = forms.CharField(widget=CKEditorUploadingWidget(attrs={'placeholder':"Type.."}))
    class Meta:
        model = Contact
        fields = ("content",)
        # widget = {"content":CKEditorWidget(attrs={"placeholder":"Type.."})}