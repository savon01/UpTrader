from django.shortcuts import render
from .models import MenuItem


def menu_view(request):
    # Определите текущий пункт меню на основе URL текущей страницы
    current_path = request.path
    selected_menu_item = MenuItem.objects.filter(url=current_path).first()

    # Получите все меню, исходя из их названия
    menu_names = MenuItem.objects.values_list('menu_name', flat=True).distinct()

    return render(request, 'menuapp/menu_view.html', {
        'menu_names': menu_names,
        'selected_menu_item': selected_menu_item,
    })


def vegetables(request):
    return render(request, 'menuapp/vegetables.html')


def fruits(request):
    return render(request, 'menuapp/fruits.html')


def computers(request):
    return render(request, 'menuapp/computers.html')


def laptops(request):
    return render(request, 'menuapp/laptops.html')
