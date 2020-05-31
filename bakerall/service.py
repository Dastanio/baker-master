# from .models import Food
# from django_filters import rest_framework as filters

"""Вычисление IP адреса пользователя"""
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

# class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
#     pass
#
# class FoodFilter(filters.FilterSet):
#     pub_date = filters.RangeFilter()
#     class Meta:
#         model = Food
#         fields = ['pub_date']