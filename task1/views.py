from django.shortcuts import render
from .models import Buyer, Game
from .forms import UserRegister  # Предположим, что форма регистрации находится в forms.py


# Представление для главной страницы
def home(request):
    return render(request, 'first_task/home.html')


# Представление для списка товаров (игр)
def shop(request):
    games = Game.objects.all()  # Получение всех игр из базы данных
    context = {'games': games}
    return render(request, 'first_task/shop.html', context)

# Представление для корзины
def cart(request):
    return render(request, 'first_task/cart.html')


# Представление регистрации через Django форму
def sign_up_by_django(request):
    users = Buyer.objects.values_list('name', flat=True)  # Получаем список всех имен пользователей
    info = {}

    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            # Проверяем данные
            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif int(age) < 18:
                info['error'] = 'Вы должны быть старше 18'
            elif username in users:
                info['error'] = 'Пользователь уже существует'
            else:
                # Создаем нового пользователя
                Buyer.objects.create(name=username, balance=0.00, age=age)
                info['success'] = f'Приветствуем, {username}!'
    else:
        form = UserRegister()

    info['form'] = form
    return render(request, 'first_task/registration_page.html', info)

# Представление регистрации через обычную HTML форму
def sign_up_by_html(request):
    users = Buyer.objects.values_list('name', flat=True)  # Получаем список всех имен пользователей
    info = {}

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = int(request.POST.get('age'))

        # Проверяем данные
        if password != repeat_password:
            info['error'] = 'Пароли не совпадают'
        elif age < 18:
            info['error'] = 'Вы должны быть старше 18'
        elif username in users:
            info['error'] = 'Пользователь уже существует'
        else:
            # Создаем нового пользователя
            Buyer.objects.create(name=username, balance=0.00, age=age)
            info['success'] = f'Приветствуем, {username}!'

    return render(request, 'first_task/registration_page.html', info)
