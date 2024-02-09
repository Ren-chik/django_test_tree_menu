## Тестовое задание

#### requirements
>Django==4.2.6
>
>asgiref==3.7.2
>
>sqlparse==0.4.4

1. python3 manage.py makemigrations menu
2. python3 manage.py migrate
3. python3 manage.py createsuperuser

#### Создание модели в admin.
Используйте поле menu_title для того что бы задать название меню, а также определите остальные поля, 
которые будут соответствовать вашим требованиям для данного меню.

Теперь используйте этот тег в ваших шаблонах
>{% load menu_tags %}
>
>{% draw_menu ‘<название меню>’ %}
