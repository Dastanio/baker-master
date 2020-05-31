from django.db import models
from rest_framework import generics
from django.core.paginator import Paginator
from .models import Food
from django.shortcuts import render
# from django_filters.rest_framework import DjangoFilterBackend
from .serializers import (
    FoodListSerializer,
    FoodDetailSerializer,
    CommentCreateSerializer,
    CreateRatingSerializer,
)
from .service import get_client_ip

class FoodListView(generics.ListAPIView):
    """Вывод списка выпечки"""
    serializer_class = FoodListSerializer
    # filter_backends = (DjangoFilterBackend,)
    # filterset_class = FoodFilter
    # permission_classes = [permissions.IsAuthenticated]


    def get_queryset(self):
        foods = Food.objects.filter(draft=False).annotate(
            rating_user=models.Count("ratings",
                                     filter=models.Q(ratings__ip=get_client_ip(self.request)))
        ).annotate(
            middle_star=models.Sum(models.F('ratings__star')) / models.Count(models.F('ratings'))
        )
        return foods

class FoodDetailView(generics.RetrieveAPIView):
    """Вывод выпечки"""
    queryset = Food.objects.filter(draft=False)
    serializer_class = FoodDetailSerializer



class CommentCreateView(generics.CreateAPIView):
    """Добавление отзыва"""
    serializer_class = CommentCreateSerializer


class AddStarRatingView(generics.CreateAPIView):
    """Добавление рейтинга к выпечке"""
    serializer_class = CreateRatingSerializer
    def perform_create(self, serializer):
        serializer.save(ip=get_client_ip(self.request))


def main(request):
    return render(request, '../templates/main.html')

def about(request):
    return render(request, '../templates/about.html')

def login(request):
    return render(request, '../templates/login.html')

def register(request):
    return render(request, '../templates/register.html')

def logout(request):
    return render(request, '../templates/logout.html')

def order(request):
    return render(request, '../templates/make_order.html')

def succ(request):
    return render(request, '../templates/suc.html')

def food_detail(request, id_food):
    a = Food.objects.get( id = id_food)
    template = '../templates/food_detail.html'
    return render(request, template, {'eda':a})

def index(request):
    foods = Food.objects.all()
    paginator = Paginator(foods, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "page_obj": page_obj
    }
    template = "../templates/index.html"
    return render(request, template, context)
