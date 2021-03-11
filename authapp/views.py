from django.shortcuts import render, HttpResponseRedirect

from authapp.forms import InfojobUserLoginForm
from authapp.forms import InfojobUserRegisterForm
from authapp.forms import InfojobUserEditForm
from django.contrib import auth
from django.urls import reverse


def login(request):
    title = 'Вход'

    login_form = InfojobUserLoginForm(data=request.POST)
    if request.method == 'POST' and login_form.is_valid():
        email = request.POST['email']
        password = request.POST['password']
        role = request.POST['role']

        user = auth.authenticate(email=email, password=password, role=role)
        if user and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('main'))

        context = {'login_form': login_form, 'title': title}
        return render(request, 'authapp/login.html', context=context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main'))
    # return HttpResponseRedirect('/')


def register(request):
    title = 'Регистрация'

    if request.method == 'POST':
        register_form = InfojobUserRegisterForm(request.POST, request.FILES)

        if register_form.is_valid():
            register_form.save()
            return HttpResponseRedirect(reverse('authapp:login'))
        else:
            register_form = InfojobUserRegisterForm()

        context = {'register_form': register_form, 'title': title}
        return render(request, 'authapp/register.html', context=context)


def edit(request):
    title = 'Редактирование'

    if request.method == 'POST':
        edit_form = InfojobUserEditForm(request.POST, request.FILES, instance=request.user)

        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('authapp:edit'))
        else:
            edit_form = InfojobUserEditForm(instance=request.user)

        context = {'edit_form': edit_form, 'title': title}
        return render(request, 'authapp/edit.html', context=context)
