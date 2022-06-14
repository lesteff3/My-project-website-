from django.db import models


class Register_on_test_drive(models.Model):
    name_person = models.CharField('Имя пользователя', max_length=50)
    phone = models.CharField('Номер телефона', max_length=12)
    car = models.CharField('Авто', max_length=30, default='')
    text = models.TextField('Причина')
    data = models.DateTimeField('Дата')

    def __str__(self):
        return self.name_person


    class Meta:
        verbose_name = 'Регистриция на ТО'
        verbose_name_plural = 'Регистриция на ТО'