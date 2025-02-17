from django.forms import ModelForm
from .models import Recipe, Category, Ingredient
from django import forms

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'ingredients', 'steps', 'cooking_time', 'image', 'author']
        labels = {
            'title': 'Название рецепта',
            'description': 'Описание',
            'ingredients': 'Ингредиенты',
            'steps': 'Шаги приготовления',
            'cooking_time': 'Время приготовления в минутах',
            'image': 'Картинка',
            'author': 'Автор',
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            # Добавляем класс "form-control" ко всем полям
            for field in self.fields.values():
                field.widget.attrs['class'] = 'form-control'


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']


class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['name']
        labels = {
            'name': 'Название ингредиента',
        }
