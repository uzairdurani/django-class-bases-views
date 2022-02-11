from django import forms
from .models import student
class AddForm(forms.ModelForm):
    class Meta:
        model = student
        fields = ('name',)
        
        widgets =  {
            'name' : forms.TextInput(attrs={'class':'form-control'})
        }
