from .models import Register_on_test_drive
from django.forms import ModelForm, TextInput, DateInput


class Register_on_test_driveForm(ModelForm):
    class Meta:
        model = Register_on_test_drive
        fields = ['name_person', 'phone', 'car', 'text', 'data']

        widgets = {
            'name_person': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ваше имя'
            }),
            'phone': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ваш номер телефона',

            }),
            'data': DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Выберите дату',
                'type': 'date'
            }),
            'car': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Автомобиль: Например Tugella',
            }),
            'text': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Причина: Например Плановое ТО',
            }),
        }