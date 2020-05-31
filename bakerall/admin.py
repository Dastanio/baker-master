from django.contrib import admin
from .models import Food, Comment, MakeAnOrder, Rating, RatingStar

admin.site.register(Food)
admin.site.register(RatingStar)
admin.site.register(Rating)
admin.site.register(Comment)
admin.site.register(MakeAnOrder)
