from django.shortcuts import render

# Create your views here.


def images_page(request):
    return render(request, "aaaaa_example.html")


def sign_in_page(request):
    return render(request, "sign_in.html")


def manage_attractions_page(request):
    return render(request, "attractions.html")


def main_page(request):
    return render(request, "main_page.html")


def add_attraction_page(request):
    return render(request, "add_attraction.html")


def error_page(request):
    return render(request, "error_page.html")


def edit_attraction_page(request):
    return render(request, "edit_attraction.html")


def add_game_page(request):
    return render(request, "add_game.html")


def more_properties_page(request):
    return render(request, "more_properties.html")


def add_game_edit_page(request):
    return render(request, "add_game_edit.html")


def add_hint_page(request):
    return render(request, "add_hint.html")


def add_hint_edit_page(request):
    return render(request, "add_hint_edit.html")


def add_aq_page(request):
    return render(request, "add_aq.html")


def add_aq_edit_page(request):
    return render(request, "add_aq_edit.html")


def pick_hint_page(request):
    return render(request, "pick_hint.html")


def pick_hint_edit_page(request):
    return render(request, "pick_hint_edit.html")


def pick_aq_edit_page(request):
    return render(request, "pick_aq_edit.html")


def edit_hint_page(request):
    return render(request, "edit_hint.html")


def edit_hint_edit_page(request):
    return render(request, "edit_hint_edit.html")


def edit_feedbacks_page(request):
    return render(request, "edit_feedbacks.html")


def feedback_page(request):
    return render(request, "feedback.html")


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


def pick_delete_game_page(request):
    return render(request, "pick_delete_game.html")


def delete_game_page(request):
    return render(request, "delete_game.html")


from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *

# Create your views here.

def hotel_image_view(request):

    if request.method == 'POST':
        form = ImagesForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ImagesForm()
    return render(request, 'hotel_image_form.html', {'form' : form})


def success(request):
	return HttpResponse('successfuly uploaded')
