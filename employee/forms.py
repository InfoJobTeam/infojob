import re
from django import forms
from django.forms.models import inlineformset_factory
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Fieldset, Div, Row, HTML, ButtonHolder, Submit
from .custom_layout_object import Formset
from .models import *


class JobExpForm(forms.ModelForm):

    class Meta:
        model = JobExp
        exclude = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        formtag_prefix = re.sub('-[0-9]+$', '', kwargs.get('prefix', ''))

        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.form_class = 'form-horizontal '
        # self.helper.label_class = 'col-md-3 create-label'
        self.helper.field_class = 'col-md-9'
        self.helper.css_class = 'formset_row-{}'.format(formtag_prefix)
        self.helper.layout = Layout(
            Row(
                Field('employer', css_class='col-md-5'),
                Field('employer_link', css_class='col-md-4')),
            Row(
                Field('position', css_class='col-md-3'),
                Field('start_at', css_class='col-md-3'),
                Field('finish_at', css_class='col-md-3')),
            Field('duties'),
        )


JobExpFormSet = inlineformset_factory(
    CV, JobExp, form=JobExpForm,
    fields=['employer', 'employer_link', 'position', 'start_at', 'finish_at', 'duties'], extra=1, can_delete=True
)


class EducationForm(forms.ModelForm):

    class Meta:
        model = Education
        exclude = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # нужно для работы JS библиотеки django-dynamic-formset
        formtag_prefix = re.sub('-[0-9]+$', '', kwargs.get('prefix', ''))


        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Row(
                Field('college_name'),
                Field('specialization'),
                Field('grade'),
                Field('graduated_at'),
                # нужно для работы JS библиотеки django-dynamic-formset
                css_class='formset_row-{}'.format(formtag_prefix)
            )
        )


EducationFormSet = inlineformset_factory(
    CV, Education, form=EducationForm,
    fields=['college_name', 'specialization', 'grade', 'graduated_at'], extra=1, can_delete=True
)





class CVForm(forms.ModelForm):

    class Meta:
        model = CV
        # fields = '__all__'
        exclude = ['is_checked', 'created_at', 'updated_at']

    def __init__(self, *args, **kwargs):
        super(CVForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal '
        self.helper.label_class = 'col-md-2 create-label'
        self.helper.field_class = 'col-md-8'
        self.helper.layout = Layout(
            Div(
                Field('user_pic'),
                Field('position_seek'),
                Field('compensation_seek'),
                Field('first_name'),
                Field('middle_name'),
                Field('family_name'),
                Field('gender'),
                Field('birthday'),
                Field('email'),
                Field('city'),
                Field('profession'),
                Field('skills'),
                Field('is_active'),
                Fieldset('Add Education',
                         Formset('edu_titles')),    #   Formset берется из custom_layout_object.py
                # Fieldset('Add Job Experience',
                #          Formset('job_titles')),
                HTML("<br>"),
                ButtonHolder(Submit('submit', 'Save')),
            )
        )
