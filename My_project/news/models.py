from django.db import models


class News(models.Model):
    title = models.CharField('Название', max_length=50)
    anons = models.CharField('Анонс', max_length=255)
    full_text = models.TextField('Текст для статьи')
    data = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.title