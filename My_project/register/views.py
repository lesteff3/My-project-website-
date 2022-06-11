from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect
from .forms import UserRegisterForm
from django.contrib.auth.models import User
from django.contrib import messages


def register(request):
    form = None
    email = request.POST.get('email')
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Пользователь с этим адресом уже зарегистрирован')
        else:
            if form.is_valid():
                ins = form.save()
                username = form.cleaned_data['username']
                password = form.cleaned_data['password1']

                user = authenticate(username=username, password=password, email=email)
                ins.email = email
                ins.save()
                form.save_m2m()
                messages.success(request, 'Вы успешно зарегистрировались')
                return redirect('/')


    else:
        form = UserRegisterForm()
    title = 'Регистрация пользователя'
    context = {'form': form,
               'title': title}
    return render(request, 'register/register.html', context=context)
