from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, FormView, DeleteView
from django.urls import reverse_lazy
from .forms import *

# Create your views here.

class create_ficha_view(CreateView):
	form_class = fichas_form
	template_name = 'create_ficha.html'
	success_url = reverse_lazy('atencion:exito')

def exito_view(request):
	return render(request,'exito.html',{})