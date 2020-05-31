from rest_framework import serializers
from .models import Food, Comment, Rating


class FilterCommentListSerializer(serializers.ListSerializer):
    """Фильтер комментарив, только parents"""
    def to_representation(self, data):
        data = data.filter(parent=None)
        return super().to_representation(data)

class RecursiveSerializer(serializers.Serializer):
    """Вывод рекурсивно children"""
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data

class FoodListSerializer(serializers.ModelSerializer):
    """Список выпечки"""
    rating_user = serializers.BooleanField()
    middle_star = serializers.IntegerField()
    class Meta:
        model = Food
        fields = ("id", "name", "composition", "description", "rating_user", "middle_star")

class CommentCreateSerializer(serializers.ModelSerializer):
    """Добавление отзыва"""
    class Meta:
        model = Comment
        fields = "__all__"

class CommentSerializer(serializers.ModelSerializer):
    """Вывод отзыва"""
    children = RecursiveSerializer(many=True)
    class Meta:
        list_serializer_class = FilterCommentListSerializer
        model = Comment
        fields = ("author", "comment_text", "children")

class FoodDetailSerializer(serializers.ModelSerializer):
    """Отдельная выпечка """
    comments = CommentSerializer(many=True)
    class Meta:
        model = Food
        exclude = ("draft",)

class CreateRatingSerializer(serializers.ModelSerializer):
    """Добавление рейтинга пользователя"""
    class Meta:
        model = Rating
        fields = ("star", "food")

    def create(self, validated_data):
        rating, _ = Rating.objects.update_or_create(
            ip=validated_data.get('ip', None),
            food=validated_data.get('food', None),
            defaults={'star': validated_data.get("star")}
        )
        return rating