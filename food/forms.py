from django.forms import ModelForm
from django import forms
from .models import Food, FoodLog


class FoodForm(ModelForm):
    class Meta:
        model = Food
        fields = ['name', 'calories', 'fat',
                  'carbohydrates', 'protein', 'quantity', 'category']
        labels = {
            'quantity': 'Quantity (gms)',
        }

    def __init__(self, *args, **kwargs):
        super(FoodForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'edit-input'})
            field.required = True
