from django.shortcuts import render, HttpResponse

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
    return HttpResponse("<h1>Приветствую</h1>")


def about(request):
    text = f"""
    Имя: <b>{author_info['name']}</b><br>
    Фамилий: <b>{author_info['surname']}</b><br>
    email: <b>{author_info['email']}<b/><br>
    """
    return HttpResponse(text)


def item_page(request, id):
    for item in items:
        if item['id'] == id:
            text = f"""
            <h2>{item['name']}</h2>
            Количество: <b>{item['quantity']}</b>
            """
            return HttpResponse(text)