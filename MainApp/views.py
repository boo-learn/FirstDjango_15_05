from django.shortcuts import render, HttpResponse
from django.http import HttpResponseNotFound

author_info = {
    "name": "Евгений",
    "surname": "Юрченко",
    "email": "eyurchenko@specialist.ru"
}

items = [
    {"id": 1, "name": "Кроссовки abibas", "quantity": 5},
    {"id": 2, "name": "Куртка кожаная", "quantity": 2},
    {"id": 5, "name": "Coca-cola 1 литр", "quantity": 12},
    {"id": 7, "name": "Картофель фри", "quantity": 0},
    {"id": 8, "name": "Кепка", "quantity": 124},
]
# /item/1
# /item/5
#

def home(request):
    return render(request, "index.html")


def about(request):
    context = {
        "author": author_info
    }
    return render(request, "about.html", context)


def item_page(request, id):
    for item in items:
        if item['id'] == id:
            context = {
                "item": item
            }
            return render(request, "item-page.html", context)
    return HttpResponseNotFound(f"Товар с id {id} не найден")


def items_list(request):
    context = {
        "items": items
    }
    return render(request, "items-list.html", context)
