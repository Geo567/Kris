from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    ListView,
    DeleteView
)

 
from .forms import MarksModelForm
from .models import Marks

class MarkseCreateView(CreateView):
    template_name = 'marks/ark_create.html'
    form_class = MarksModelForm
    queryset = Marks.objects.all() # <blog>/<modelname>_list.html
    #success_url = '/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

    #def get_success_url(self):
    #    return '/'

 