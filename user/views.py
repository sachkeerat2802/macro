from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import RegisterUserCreationForm, ProfileForm, WeightLogForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import WeightLog
from food.models import FoodLog, Food
from .utils import convert


def index(request):
    if request.user.is_authenticated:
        return redirect('overview')
    else:
        return redirect('login')


def register_user(request):
    if request.user.is_authenticated:
        return redirect('overview')

    form = RegisterUserCreationForm()

    if request.method == "POST":
        form = RegisterUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('edit-account')
        else:
            messages.error(request, "An unexpected error occurred!")

    context = {'form': form}
    return render(request, 'user/register.html', context)


def login_user(request):
    if request.user.is_authenticated:
        return redirect('overview')

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            return redirect('index')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('overview')
        else:
            return redirect('index')

    return render(request, 'user/login.html')


def logout_user(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == "POST":
        logout(request)
        return redirect('login')

    return render(request, 'user/logout.html')


@login_required(login_url='login')
def user_overview(request):
    user = request.user
    profile = user.profile
    user_food = Food.objects.filter(user=user)

    if request.method == "POST":
        food = request.POST['foodlog']
        print(food)
        if food != "choose here":
            food_consumed = Food.objects.get(name=food, user=user)
            new_log = FoodLog(user=user, food=food_consumed)
            new_log.save()
            return redirect('overview')

    logs = FoodLog.objects.filter(user=user)
    calories = 0
    fat = 0
    carbohydrates = 0
    protein = 0

    for log in logs:
        calories += log.food.calories
        fat += log.food.fat
        carbohydrates += log.food.carbohydrates
        protein += log.food.protein

    context = {'profile': profile, 'logs': logs, 'calories': calories,
               'fat': fat, 'carbohydrates': carbohydrates, 'protein': protein, 'user_food': user_food}
    return render(request, 'user/overview.html', context)


@login_required(login_url='login')
def view_account(request):
    user = request.user
    profile = user.profile
    form = WeightLogForm()

    if request.method == "POST":
        form = WeightLogForm(request.POST)

        if form.is_valid():
            new_weight = form.save(commit=False)
            new_weight.user = user
            new_weight.save()

            latest_weight = WeightLog.objects.filter(
                user=user).order_by('-entry_date').first()

            if latest_weight is not None:
                profile.weight = latest_weight.weight
                profile.save()
            else:
                profile.weight = None
                profile.save()

            return redirect('account')

    weights = WeightLog.objects.filter(user=user)
    context = {'weights': weights, 'profile': profile, 'form': form}
    return render(request, 'user/account.html', context)


@login_required(login_url='login')
def edit_account(request):
    user = request.user
    profile = user.profile
    form = ProfileForm(instance=profile)

    if request.method == "POST":
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            if 'metric' in form.changed_data:
                convert(profile)

            latest_weight = WeightLog.objects.filter(
                user=user).order_by('-entry_date').first()

            if latest_weight is not None:
                profile.weight = latest_weight.weight
                profile.save()
            else:
                profile.weight = None
                profile.save()

            return redirect('account')

    context = {'form': form}
    return render(request, 'user/edit-account.html', context)


@login_required(login_url='login')
def weight_edit(request, pk):
    user = request.user
    profile = user.profile
    weight = WeightLog.objects.get(id=pk)
    form = WeightLogForm(instance=weight)

    if request.method == "POST":
        form = WeightLogForm(request.POST, instance=weight)
        if form.is_valid():
            form.save()

            latest_weight = WeightLog.objects.filter(
                user=user).order_by('-entry_date').first()

            if latest_weight is not None:
                profile.weight = latest_weight.weight
                profile.save()
            else:
                profile.weight = None
                profile.save()

            return redirect('account')

    context = {'form': form, 'weight': weight}
    return render(request, 'user/edit-weightlog.html', context)


@login_required(login_url='login')
def weight_delete(request, pk):
    user = request.user
    profile = user.profile
    weight = WeightLog.objects.get(id=pk)

    if request.method == "POST":
        weight.delete()

        latest_weight = WeightLog.objects.filter(
            user=user).order_by('-entry_date').first()

        if latest_weight is not None:
            profile.weight = latest_weight.weight
            profile.save()
        else:
            profile.weight = None
            profile.save()

        return redirect('account')

    context = {'weight': weight, 'profile': profile}
    return render(request, 'user/delete-weightlog.html', context)


@login_required(login_url='login')
def delete_foodlog(request, pk):
    log = FoodLog.objects.get(id=pk)

    if request.method == "POST":
        log.delete()
        return redirect('overview')

    context = {'log': log}
    return render(request, 'food/delete-foodlog.html', context)


@login_required(login_url='login')
def clear_foodlogs(request):
    if request.method == "POST":
        FoodLog.objects.all().delete()
        return redirect('overview')

    return render(request, 'food/clear-foodlogs.html')
