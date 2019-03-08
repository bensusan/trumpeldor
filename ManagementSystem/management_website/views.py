from django.shortcuts import render

# Create your views here.


def sign_in_page(request):
    return render(request, "sign_in.html")


def manage_attractions_page(request):
    return render(request, "attractions.html")


def main_page(request):
    return render(request, "main_page.html")
