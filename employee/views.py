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
        context['collections'] = CV.objects.order_by('id')
        return context


##########################################################################
#                           CV  views                           #
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
        data = super(CvCreate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['edu_titles'] = EducationFormSet(self.request.POST)
        else:
            data['edu_titles'] = EducationFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        titles = context['titles']
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
            data['edu_titles'] = EducationFormSet(self.request.POST, instance=self.object)
        else:
            data['edu_titles'] = EducationFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        titles = context['edu_titles']
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
    success_url = reverse_lazy('mycollections:homepage')



def employee(request):
    return render(request, 'employee/employee.html')