from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse
from .forms import SchoolboysModelForm
from .models import Schoolboys
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    ListView,
    DeleteView
)


#def posts_list(request):
   # return render (request, "schoolboys/index.html")
   # print()


def index(request):
    return render (request, "schoolboys/index.html")
   # print()

#def index(request):
    #return HttpResponse("<center><h1>Hello, Worldghfghfhftghg</h1>")
   # print()
   # print()
   # print(request)
   # print() 
   # print(dir(request))
   # pass

class SchoolboysCreateView(CreateView):
    template_name = 'schoolboys/schoolboys_create.html'
    form_class = SchoolboysModelForm
    queryset = Schoolboys.objects.all() # <blog>/<modelname>_list.html
    #success_url = '/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

    #def get_success_url(self):
    #    return '/'


# Create your views here.
