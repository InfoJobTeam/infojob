from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# from .forms import *
from .models import *
from django.db import transaction
from django.http import HttpResponse



class EmployerView(TemplateView):
    template_name = "employer/employer_dash.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['collections'] = Vacancy.objects.order_by('id')
        return context


def employer(request):
    return render(request, 'employer/employer.html')