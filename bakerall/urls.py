from django.urls import path
from . import views

urlpatterns = [
    path('food/', views.FoodListView.as_view()),
    path('food/>/', views.FoodDetailView.as_view()),
    path('food_detail/<int:id_food>/', views.food_detail, name='food_detail'),
    path('comment/', views.CommentCreateView.as_view()),
    path('rating/', views.AddStarRatingView.as_view()),
    path('order/', views.order, name="order"),
    path('menu/',  views.index, name="index"),
    path('', views.main, name="main"),
    path('about/', views.about, name="about"),
]