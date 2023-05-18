from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponseNotFound
from MainApp.models import Item
from django.core.exceptions import ObjectDoesNotExist

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
    try:
        item = Item.objects.get(id=id)
        colors = item.colors.all()
    except ObjectDoesNotExist:
        return HttpResponseNotFound(f"Товар с id {id} не найден")
    context = {
        "item": item,
        "colors": colors
    }
    return render(request, "item-page.html", context)


def items_list(request):
    items = Item.objects.all()
    context = {
        "items": items
    }
    return render(request, "items-list.html", context)


def item_add(request):
    if request.method == "GET":
        return render(request, "item-add.html")


# Получаем данные от формы
def item_create(request):
    if request.method == "POST":
        form_data = request.POST
        colors_id = form_data.getlist("colors")
        item = Item(
            name=form_data['name'],
            brand=form_data['brand'],
            count=form_data['count'],
        )
        item.save()
        return redirect('items-list')
        # print(f"{form_data=}")
