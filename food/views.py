from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Food
from .forms import FoodForm


@login_required(login_url='login')
def add_food(request):
    form = FoodForm()

    if request.method == "POST":
        form = FoodForm(request.POST)

        if form.is_valid():
            new_food = form.save(commit=False)
            new_food.user = request.user
            new_food.save()
            return redirect('food-list')

    context = {'form': form}
    return render(request, 'food/add-food.html', context)


@login_required(login_url='login')
def food_list(request):
    foods = Food.objects.filter(user=request.user)
    context = {'foods': foods}
    return render(request, 'food/food-list.html', context)


@login_required(login_url='login')
def view_food(request, pk):
    food = Food.objects.get(id=pk)
    context = {'food': food}
    return render(request, 'food/food.html', context)


@login_required(login_url='login')
def edit_food(request, pk):
    food = Food.objects.get(id=pk)
    form = FoodForm(instance=food)

    if request.method == "POST":
        form = FoodForm(request.POST, instance=food)
        if form.is_valid():
            form.save()
            return redirect('food', pk=food.id)

    context = {'food': food, 'form': form}
    return render(request, 'food/food-edit.html', context)


@login_required(login_url='login')
def delete_food(request, pk):
    food = Food.objects.get(id=pk)

    if request.method == "POST":
        food.delete()
        return redirect('food-list')

    context = {'food': food}
    return render(request, 'food/food-delete.html', context)
