from django import forms
from .models import Marks


class MarksModelForm(forms.ModelForm):
    class Meta:
        model = Marks
        fields =[
            'usere',
            'lesson',
            'mark',
            'index',
            'date_receiv',
        ]           


     