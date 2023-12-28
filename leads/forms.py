from django import forms
from .models import Leads
class LeadModelForm(forms.ModelForm):
    class Meta:
        model = Leads
        fields = ('first_name','last_name','Age','agent'
        )



class LeadForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    age = forms.IntegerField(min_value=0)