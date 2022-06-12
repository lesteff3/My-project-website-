from django.db import models


class Register_on_test_drive(models.Model):
    name_person = models.CharField('Имя пользователя', max_length=50)
    phone = models.CharField('Номер телефона', max_length=12)
    data = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.name_person


    class Meta:
        verbose_name = 'Регистриция на тест-драйв'
        verbose_name_plural = 'Регистриция на тест-драйв'