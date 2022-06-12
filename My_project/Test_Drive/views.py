from django.shortcuts import render, redirect
from .models import Register_on_test_drive
from .forms import Register_on_test_driveForm


def register_on_test_drive(request):
    error = ''
    if request.method == 'POST':
        form = Register_on_test_driveForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register_person')
        else:
            error = 'Форма была неверной'

    form = Register_on_test_driveForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'test_drive/test_drive.html', data)

def registers_person(request):
    text = 'Ваша заявка успешно обработана!!!'
    one_more_text = 'в ближайшее время c вами свяжется менеджер'
    return_text = {
        'text': text,
        'one_more_text': one_more_text
    }
    return render(request, 'test_drive/person_who_register_on_test.html', return_text)