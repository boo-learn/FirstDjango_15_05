from django.shortcuts import render, HttpResponse
from django.http import HttpResponseNotFound
from MainApp.models import Item

author_info = {
    "name": "Евгений",
    "surname": "Юрченко",
    "email": "eyurchenko@specialist.ru"
}


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
    items = Item.objects.all()
    context = {
        "items": items
    }
    return render(request, "items-list.html", context)
