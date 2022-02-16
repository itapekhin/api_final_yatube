# API проекта Yatube (v1)

Подробная документация проекта расположена по ссылке:
```
http://127.0.0.1:8000/redoc/
```
### Примечание: Для получения доступа к документации необходимо осуществить запуск проекта в соответствии с инструкцией ниже!!!

## Описание

API проекта Yatube (v1) - API приложение блога Yatube, дает возможность пользователям блога управлять (просмотр, создание, изменение и удаление) своими публикациями, просматривать публикации других пользователей, осуществлять подписку на авторов и комментировать посты. Основная задача предоставить пользователям возможность создавать приложения для управления и просмотра контента,а так же формировать требуемую статистику с использованием любого языка программирования.

## Запуск проекта на локальной машине:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/itapekhin/api_final_yatube.git
```

```
cd yatube_api
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

```
source venv/Script/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```
## Некоторые примеры запросов к API:
Получить список всех постов:

```
GET http://127.0.0.1:8000/api/v1/posts/ 
```

Создать новый пост с текстом "Hellow Word" и определить его в группу с id=1:

```
POST http://127.0.0.1:8000/api/v1/posts/
Content-Type: application/json
Authorization: Bearer eyJ0eXAiO....

{
    "text": "Hellow Word",
    "group": 1
}
```

Вывести список всех комментариев к посту с id=1:

```
GET http://127.0.0.1:8000/api/v1/posts/1/comments/
```

Создать новый комментарий с текстом "Hellow Word" к посту с id=3 с:

```
POST http://127.0.0.1:8000/api/v1/posts/1/comments/
Content-Type: application/json
Authorization: Bearer eyJ0eXAiO....

{
    "text": "Hellow Word"
}
```

Вывести список сообществ:

```
GET http://127.0.0.1:8000/api/v1/groups/
```

Получение информации о сообществе c id=3:

```
GET http://127.0.0.1:8000/api/v1/groups/3/
```

Получить список подписок текущего пользователя:

```
GET http://127.0.0.1:8000/api/v1/follow/
Content-Type: application/json
Authorization: Bearer eyJ0eXAiO....
```

Подписаться на автора с логином "Pumba":

```
POST http://127.0.0.1:8000/api/v1/follow/
Content-Type: application/json
Authorization: Bearer eyJ0eXAiO....

{
    "following": "Pumba"
}
```
