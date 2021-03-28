from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import CollectionTitleFormSet, CollectionForm
from .models import CV, JobExp
from django.db import transaction
from django.http import HttpResponse


# ['collections'] - relation name
# ['title'] - Formset('title')


class HomepageView(TemplateView):
    template_name = "employee/base.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # [relation_name]
        context['cv'] = CV.objects.order_by('id')
        return context


##########################################################################
#                           Collection views                             #
##########################################################################

class CollectionDetailView(DetailView):
    model = CV
    template_name = 'employee/cv_detail.html'

    def get_context_data(self, **kwargs):
        context = super(CollectionDetailView, self).get_context_data(**kwargs)
        return context


class CollectionCreate(CreateView):
    model = CV
    template_name = 'employee/cv_create.html'
    form_class = CollectionForm
    success_url = None

    def get_context_data(self, **kwargs):
        data = super(CollectionCreate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['title'] = CollectionTitleFormSet(self.request.POST)
        else:
            data['title'] = CollectionTitleFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        print(f'context {context}')
        titles = context['title']
        with transaction.atomic():
            form.instance.created_by = self.request.user
            self.object = form.save()
            if titles.is_valid():
                titles.instance = self.object
                titles.save()
        return super(CollectionCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('employee:cv_detail', kwargs={'pk': self.object.pk})


    # @method_decorator(login_required)
    # def dispatch(self, *args, **kwargs):
    #     return super(CollectionCreate, self).dispatch(*args, **kwargs)


class CollectionUpdate(UpdateView):
    model = CV
    form_class = CollectionForm
    template_name = 'employee/cv_create.html'

    def get_context_data(self, **kwargs):
        data = super(CollectionUpdate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['title'] = CollectionTitleFormSet(self.request.POST, instance=self.object)
        else:
            data['title'] = CollectionTitleFormSet(instance=self.object)
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
        return super(CollectionUpdate, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('employee:cv_detail', kwargs={'pk': self.object.pk})

    # @method_decorator(login_required)
    # def dispatch(self, *args, **kwargs):
    #     return super(CollectionUpdate, self).dispatch(*args, **kwargs)


class CollectionDelete(DeleteView):
    model = CV
    template_name = 'employee/confirm_delete.html'
    success_url = reverse_lazy('employee:employee')