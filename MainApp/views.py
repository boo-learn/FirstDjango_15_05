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
            text = f"""
            <h2>{item['name']}</h2>
            Количество: <b>{item['quantity']}</b>
            <a href='/items/'>Назад</a>
            """
            return HttpResponse(text)
    return HttpResponseNotFound(f"Товар с id {id} не найден")


def items_list(request):
    text = "<h2>Список товаров</h2><ol>"
    for item in items:
        text += f"<a href='/item/{item['id']}/'><li>{item['name']}</li></a>"
    text += "</ol>"
    return HttpResponse(text)
