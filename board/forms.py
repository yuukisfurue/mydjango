from django import forms
from.models import Member

class BoardForm(forms.Form):
    name = forms.CharField(label='Name', \
        widget=forms.TextInput(attrs={'class':'form-control'}))
    prefecture = forms.CharField(label='Prefecture', \
        widget=forms.TextInput(attrs={'class':'form-control'}))
    gender = forms.BooleanField(label='Gender', required=False, \
        widget=forms.CheckboxInput(attrs={'class':'form-check'}))
    employmentstatus = forms.CharField(label='EMPLOYMENTSTATUS', \
        widget=forms.TextInput(attrs={'class':'form-control'}))
    company = forms.CharField(label='COMPANY', \
        widget=forms.CheckboxInput(attrs={'class':'form-check'}))
    jyob = forms.CharField(label='Jyob', \
        widget=forms.TextInput(attrs={'class':'form-control'}))
    stay = forms.CharField(label='Stays', \
        widget=forms.CheckboxInput(attrs={'class':'form-check'}))
    affiliation = forms.CharField(label='Affiliation', \
        widget=forms.TextInput(attrs={'class':'form-control'}))
    postion = forms.CharField(label='Postion', \
        widget=forms.TextInput(attrs={'class':'form-control'}))
    annual = forms.CharField(label='Annual', \
        widget=forms.TextInput(attrs={'class':'form-control'}))
    lastyear = forms.CharField(label='Lastyear', \
        widget=forms.TextInput(attrs={'class':'form-control'}))

class CheckForm(forms.Form):
    str = forms.CharField(label='String', \
        widget=forms.TextInput(attrs={'class':'form-control'}))
    
    def clean(self):
        cleaned_data = super().clean()
        str = cleaned_data['str']
        if (str.lower().startswith('no')):
            raise forms.ValidationError('You input "NO"!')

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['name','prefecture','gender','employmentstatus','company','jyob','stay','affiliation','postion','annual','lastyear']


class FindForm(forms.Form):
    find = forms.CharField(label='Find', required=False, \
        widget=forms.TextInput(attrs={'class':'form-control'}))



