from django import forms
from.models import Member

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['name','age','gender','pref','jyob','pojishon']

class CheckForm(forms.Form):
    str = forms.CharField(label='Name',\
        widget=forms.TextInput(attrs={'class':'form-control'}))

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['name','age','gender','pref','jyob','pojishon']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'age': forms.TextInput(attrs={'class':'form-control'}),
            'gender': forms.TextInput(attrs={'class':'form-control'}),
            'pref': forms.TextInput(attrs={'class':'form-control'}),
            'jyob': forms.TextInput(attrs={'class':'form-control'}),
            'pojishon': forms.TextInput(attrs={'class':'form-control'}),
        }
class CheckForm(forms.Form):
    str = forms.CharField(label='String', \
        widget=forms.TextInput(attrs={'class':'form-control'}))
    
    def clean(self):
        cleaned_data = super().clean()
        str = cleaned_data['str']
        if (str.lower().startswith('no')):
            raise forms.ValidationError('You input "NO"!')
