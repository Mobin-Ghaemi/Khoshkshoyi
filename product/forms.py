from django import forms
from product import models

class SabteSefaresh(forms.ModelForm):
    class  Meta : 

        model=models.sefaresh
        fields='__all__'
    