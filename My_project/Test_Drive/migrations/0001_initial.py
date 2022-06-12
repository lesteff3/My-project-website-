# Generated by Django 4.0.4 on 2022-06-12 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register_on_test_drive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_person', models.CharField(max_length=50, verbose_name='Имя пользователя')),
                ('phone', models.IntegerField(max_length=25, verbose_name='Номер телефона')),
                ('data', models.DateTimeField(verbose_name='Дата публикации')),
            ],
            options={
                'verbose_name': 'Регистриция на тест-драйв',
                'verbose_name_plural': 'Регистриция на тест-драйв',
            },
        ),
    ]