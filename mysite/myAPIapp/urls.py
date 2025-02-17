from django.urls import path
from .views import hello_world_view, RecipeView

app_name = "myAPIapp"
urlpatterns = [
    path("hello/", hello_world_view, name="hello"),
    path("recipes/", RecipeView.as_view(), name="recipes"),
    ]