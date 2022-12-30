from django.contrib import admin
from .models import Food, FoodCategory, FoodLog

admin.site.register(Food)
admin.site.register(FoodCategory)
admin.site.register(FoodLog)
