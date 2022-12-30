from urllib import request
from django.db import models
from django.contrib.auth.models import User
import uuid


class FoodCategory(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class Food(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    calories = models.IntegerField()
    fat = models.DecimalField(
        max_digits=7, decimal_places=2)
    carbohydrates = models.DecimalField(
        max_digits=7, decimal_places=2)
    protein = models.DecimalField(
        max_digits=7, decimal_places=2)
    quantity = models.IntegerField()
    category = models.ForeignKey(
        FoodCategory, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.name


class FoodLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return f"{self.user.first_name} had {self.food.name}"
