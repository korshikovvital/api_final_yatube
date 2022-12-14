# api_final
Финальный проект спринта: Проект «API для Yatube»
Задание

Реализовать API для приложения Yatube
Описание

Этот проект позволяет пользоваться приложением Yatube:

    получение списка публикаций или отдельной публикации по id
    добавление, обновление, удаление публикаций
    получение списка доступных сообществ и получение информации о сообществе по id
    получение всех комментариев к публикации или комментария к публикации по id
    добавление, обновление, удаление комментариев
    подписывание на пользователей

Использованные технологии

    Python 3.9
    Django 2.2.16
    Django Rest Framework 3.12.4
    Simple-JWT 4.7.2
    
Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

git clone https://github.com/korshikovvital/api_final_yatube.git

cd api_final_yatube

Cоздать и активировать виртуальное окружение:

python3 -m venv env

source env/bin/activate

python3 -m pip install --upgrade pip

Установить зависимости из файла requirements.txt:

pip install -r requirements.txt

Выполнить миграции:

python3 manage.py migrate

Запустить проект:

python3 manage.py runserver


Примеры

GET http://127.0.0.1:8000/api/v1/posts/  Http status 200,
POST http://127.0.0.1:8000/api/v1/posts/ Http status 201

Подробная документация с примерами размещена по адресу: http://127.0.0.1:8000/redoc/
Автор

Коршиков Виталий

    korshikovvitaly@gmail.com
    https://t.me/Spb_vitaliy_korshikov
