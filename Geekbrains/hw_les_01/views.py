from django.shortcuts import render
from django.http import HttpResponse
import logging
from random import choice, randint

logger = logging.getLogger(__name__)

def index(request):
    logger.info('Index page accessed')
    return HttpResponse('<!DOCTYPE html> <html lang="en"> <head> <meta charset="UTF-8">' \
                        '<meta name="viewport" content="width=device-width, initial-scale=1.0">' \
                        '<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">' \
                        '<body style="background-image: url(https://img1.akspic.ru/attachments/originals/6/1/6/4/7/174616-minimalizm-operacionnaya_sistema-oblako-zhest-gaz-7680x4320.jpg);background-size: cover;">' \
                        '<title> Главная страница </title> </head> <body>' \
                        '<header class="mb-auto"> <div>' \
                        '<nav class="nav nav-masthead justify-content-center float-md-end"> <a class="nav-link" href="/about">О себе</a>' \
                        '</nav> </div> </header>' \
                        '<main class="px-3"> <h1>Приветствую тебя, пользователь!</h1>' \
                        '<p class="lead">Эти страницы сделаны в рамках домашнего задания по изучению фреймворка ' \
                        'Django - Урок 1. Введение в Django. </p>' \
                        '</p> </main>' \
                        '<footer class="modal-footer"> <p>(c) Руслан Альбаков, 2023</p> </footer> </body> </html>')

def about(request):
    logger.info('About page accessed')
    return HttpResponse('<!DOCTYPE html> <html lang="en"> <head> <meta charset="UTF-8">' \
                        '<meta name="viewport" content="width=device-width, initial-scale=1.0">' \
                        '<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">' \
                        '<body style="background-image: url(https://img1.akspic.ru/attachments/originals/6/1/6/4/7/174616-minimalizm-operacionnaya_sistema-oblako-zhest-gaz-7680x4320.jpg);background-size: cover;">' \
                        '<title> О себе </title> </head> <body>' \
                        '<header class="mb-auto"> <div>' \
                        '<nav class="nav nav-masthead justify-content-center float-md-end"> <a class="nav-link" href="/">На главную</a>' \
                        '</nav> </div> </header>' \
                        '<main class="px-3"> <h1>Это страница об Альбакове Руслане.</h1>' \
                        '<p class="lead">Привет, как ты понял, меня зовут Руслан. Мне 32 и являюсь студентом Geekbrans, факультета Python-разработчик.</p>' \
                        '</p> </main>' \
                        '<footer class="modal-footer"> <p>(c) Руслан Альбаков, 2023</p> </footer> </body> </html>')