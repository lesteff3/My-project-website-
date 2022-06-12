from django.db import models


class Models_car(models.Model):
    name_auto = models.CharField('Модель автомобиля', max_length=50)
    text_about_auto = models.TextField('Описание автомобиля')
    photo = models.ImageField('Фото авто', upload_to='photos/%Y/%n/%d/')
    data = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.name_auto


    class Meta:
        verbose_name = 'Каталог'
        verbose_name_plural = 'Каталог авто'