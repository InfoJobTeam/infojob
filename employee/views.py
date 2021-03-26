from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import *
from .models import *
from django.db import transaction
from django.http import HttpResponse



class EmployeeView(TemplateView):
    template_name = "employee/employee_dash.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cv'] = CV.objects.order_by('id')
        return context


##########################################################################
#                           Collection views                             #
##########################################################################

class CvDetailView(DetailView):
    model = CV
    template_name = 'employee/cv_detail.html'

    def get_context_data(self, **kwargs):
        context = super(CvDetailView, self).get_context_data(**kwargs)
        return context


class CvCreate(CreateView):
    model = CV
    template_name = 'employee/cv_create.html'
    form_class = CVForm
    success_url = None

    def get_context_data(self, **kwargs):
        print("Im POST-1")
        data = super(CvCreate, self).get_context_data(**kwargs)
        print("Im POST-2")
        if self.request.POST:
            data['title'] = JobExpFormSet(self.request.POST)
            print("Im POST-3")
        else:
            data['title'] = JobExpFormSet()
            print("Im GET from get_context_data")
        print(f'Im DATA {data}')
        return data

    print('pre-value')

    def form_valid(self, form):
        print('Valid-1')
        context = self.get_context_data()
        print(f'Im context {context}')
        titles = context['title']
        with transaction.atomic():
            form.instance.created_by = self.request.user
            self.object = form.save()
            if titles.is_valid():
                titles.instance = self.object
                titles.save()
        return super(CvCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('employee:cv_detail', kwargs={'pk': self.object.pk})


    # @method_decorator(login_required)
    # def dispatch(self, *args, **kwargs):
    #     return super(CollectionCreate, self).dispatch(*args, **kwargs)


class CvUpdate(UpdateView):
    model = CV
    form_class = CVForm
    template_name = 'employee/cv_create.html'

    def get_context_data(self, **kwargs):
        data = super(CvUpdate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['title'] = JobExpFormSet(self.request.POST, self.request.FILES, instance=self.object)
        else:
            data['title'] = JobExpFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        titles = context['title']
        with transaction.atomic():
            form.instance.created_by = self.request.user
            self.object = form.save()
            if titles.is_valid():
                titles.instance = self.object
                titles.save()
        return super(CvUpdate, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('employee:cv_detail', kwargs={'pk': self.object.pk})

    # @method_decorator(login_required)
    # def dispatch(self, *args, **kwargs):
    #     return super(CollectionUpdate, self).dispatch(*args, **kwargs)


class CvDelete(DeleteView):
    model = CV
    template_name = 'employee/confirm_delete.html'
    success_url = reverse_lazy('employee:employee')