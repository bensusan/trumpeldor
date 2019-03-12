from django.shortcuts import render

# Create your views here.


def sign_in_page(request):
    return render(request, "sign_in.html")


def manage_attractions_page(request):
    return render(request, "attractions.html")


def main_page(request):
    return render(request, "main_page.html")


def add_attraction_page(request):
    return render(request, "add_attraction.html")


def edit_attraction_page(request):
    return render(request, "edit_attraction.html")


def add_game_page(request):
    return render(request, "add_game.html")


def add_short_path_page(request):
    return render(request, "add_short_path.html")


def info_page(request):
    return render(request, "add_info.html")