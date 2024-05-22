from django.shortcuts import render, HttpResponse
from django.http import HttpResponseNotFound

author = {
    "name": "Василий",
    "surname": "Задорнов",
    "fio": "Василий П.З.",
    "phone": "+79007001122",
    "mail": "vpz@mail.ru",
}

items = [
   {"id": 1, "name": "Кроссовки abibas", "quantity": 5},
   {"id": 2, "name": "Куртка кожаная", "quantity": 2},
   {"id": 5, "name": "Coca-cola 1 литр", "quantity": 12},
   {"id": 7, "name": "Картофель фри", "quantity": 0},
   {"id": 8, "name": "Кепка", "quantity": 124},
]


def home(request):
    text = f"""
    <h1>"Изучаем django"</h1>
    <strong>Автор</strong>: <i>{author["fio"]}</i>
    <a href='/items/'>Список товаров</a>
    """
    return HttpResponse(text)


def about(request):
    text = f"""
    Имя: <b>{author["name"]}</b><br>
    Фамилия: <b>{author["surname"]}</b><br>
    телефон: <b>{author["phone"]}</b><br>
    email: <b>{author["mail"]}</b><br>
    """
    return HttpResponse(text)


def item_page(request, item_id):
    for item in items:
        if item['id'] == item_id:
            text = f"""<h2>{item['name']}</h2>
            количество: {item['quantity']}
            <a href='/items/'>Назад</a>
            """
            return HttpResponse(text)

    return HttpResponseNotFound(f'Товар с id={item_id} не найден')


def items_list(request):
    text = """<h2>Список товаров</h2>
    <ul>
    """
    for item in items:
        text += f"<li><a href='/item/{item['id']}'>{item['name']}</a></li>"
    text += '</ul>'
    return HttpResponse(text)
