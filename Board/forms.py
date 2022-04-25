from django import forms

class BoardForm(forms.Form):
    id = forms.IntegerField(label='ID')