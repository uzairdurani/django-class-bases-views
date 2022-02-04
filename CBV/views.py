from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import student

# Create your views here.
class newPage(TemplateView):
    template_name = 'newPage.html'
    def get_context_data(self, **kwargs):
      context =  super().get_context_data(**kwargs)
      context['student']  = student.objects.get(id = 1)
      context['data'] = 'Name From Student Model'
      return context
