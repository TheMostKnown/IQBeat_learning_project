from django import forms


class DocumentForm(forms.Form):
     key = forms.CharField(max_length=200)
     file = forms.FileField()