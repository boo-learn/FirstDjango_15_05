from django.shortcuts import render, HttpResponse

author_info = {
    "name": "Евгений",
    "surname": "Юрченко",
    "email": "eyurchenko@specialist.ru"
}


def home(request):
    return HttpResponse("<h1>Приветствую</h1>")


def about(request):
    text = f"""
    Имя: <b>{author_info['name']}</b><br>
    Фамилий: <b>{author_info['surname']}</b><br>
    email: <b>{author_info['email']}<b/><br>
    """
    return HttpResponse(text)
