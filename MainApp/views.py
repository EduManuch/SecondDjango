from django.shortcuts import render
from django.http import HttpResponseNotFound
from MainApp.models import Item
from django.core.exceptions import ObjectDoesNotExist

author = {
    "name": "Василий",
    "surname": "Задорнов",
    "fio": "Василий П.З.",
    "phone": "+79007001122",
    "mail": "vpz@mail.ru",
}


def home(request):
    context = {
        'name': author['name'],
        'surname': author['surname'],
        'fio': author['fio']
    }
    return render(request, 'index.html', context)


def about(request):
    context = {
        'author': author
    }
    return render(request, 'about.html', context)


def item_page(request, item_id):
    try:
        item = Item.objects.get(id=item_id)
    except ObjectDoesNotExist:
        return HttpResponseNotFound(f'Товар с id={item_id} не найден')
    context = {
        'item': item
    }
    return render(request, 'item-page.html', context)


def items_list(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'item-list.html', context)
