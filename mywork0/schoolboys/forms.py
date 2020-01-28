from django import forms

from .models import Schoolboys


class SchoolboysModelForm(forms.ModelForm):
    class Meta:
        model = Schoolboys
        fields =[
            'name',
            'mail',
            'school',
            'level',
            'password',
            'fiscul',
            'lit',
            'algebra',
            'geomet',
            'history',
            'fiscul_t',
            'lit_t',
            'algebra_t',
            'geomet_t',
            'history_t',
        ]
