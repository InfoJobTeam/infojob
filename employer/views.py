from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
# from .forms import *
from .models import *
from django.db import transaction
from django.http import HttpResponse



class HomepageView(TemplateView):
    template_name = "employer/employer.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['company'] = Company.objects.order_by('id')
        context['have_invitation'] = Vacancy.objects.order_by('id')
        return context


class CollectionCreate(CreateView):
    pass



class CompanyDetail(DetailView):
    model = Company
    context_object_name = 'company'
    template_name = 'employer/company_detail.html'


class CompanyCreate(CreateView):
    model = Company
    exclude = ['created_at', 'updated_at']
    success_url = None

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CompanyCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('employer:company_detail', kwargs={'pk': self.object.pk})


class CompanyUpdate(UpdateView):
    model = Company
    exclude = ['created_at', 'updated_at']
    success_url = None

    def get_success_url(self):
        return reverse_lazy('employer:company_detail', kwargs={'pk': self.object.pk})


class CompanyDelete(DeleteView):
    model = Company
    context_object_name = 'company'
    success_url = reverse_lazy('employer:employer')

