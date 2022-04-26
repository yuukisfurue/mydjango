from django import forms

class BoardForm(forms.Form):
    name = forms.CharField(label='Name', \
        widget=forms.TextInput(attrs={'class':'form-control'}))
    age = forms.IntegerField(label='Age', \
        widget=forms.NumberInput(attrs={'class':'form-control'}))
    gender = forms.CharField(label='Gender', required=False, \
        widget=forms.TextInput(attrs={'class':'form-control'}))
    pref = forms.CharField(label='Pref', \
        widget=forms.TextInput(attrs={'class':'form-control'})) 
    jyob = forms.CharField(label='Jyob', \
        widget=forms.TextInput(attrs={'class':'form-control'}))
    pojishon = forms.CharField(label='Pojishon', \
        widget=forms.TextInput(attrs={'class':'form-control'}))    
