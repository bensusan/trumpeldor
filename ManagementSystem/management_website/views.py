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


def add_hint_page(request):
    return render(request, "add_hint.html")


def add_aq_page(request):
    return render(request, "add_aq.html")


def pick_hint_page(request):
    return render(request, "pick_hint.html")


def edit_hint_page(request):
    return render(request, "edit_hint.html")


def add_picture_page(request):
    return render(request, "add_picture.html")


def add_path_page(request):
    return render(request, "add_path.html")


def pick_aq_page(request):
    return render(request, "pick_aq.html")


def pick_path_edit_page(request):
    return render(request, "pick_path_edit.html")


def pick_path_delete_page(request):
    return render(request, "pick_path_delete.html")


def add_short_path_page(request):
    return render(request, "add_short_path.html")


def add_medium_path_page(request):
    return render(request, "add_medium_path.html")


def add_long_path_page(request):
    return render(request, "add_long_path.html")


def edit_short_path_page(request):
    return render(request, "edit_short_path.html")


def edit_medium_path_page(request):
    return render(request, "edit_medium_path.html")


def edit_long_path_page(request):
    return render(request, "edit_long_path.html")


def info_page(request):
    return render(request, "add_info.html")