from django.contrib import admin
from .models import Dish,Cuisine,Meal,Unit,Currency,Registration,Comment,Restaurant,Comment_of_Restaurant
from django.contrib.sessions.models import Session
from django.utils.html import format_html
from django.utils.safestring import mark_safe
class DishesAdmin(admin.ModelAdmin):
    list_display = ["id","IN","name","rating","price","mass_of_meal","image","consist","description","is_active"]
    readonly_fields = ("image",)
    def image(self, obj):
        return mark_safe(f'<img src="{obj.image_of_meal.url}" width="300" height="300"')
    image.short_description = "Image"
class CustomersAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Registration._meta.fields]
    search_fields = ["name","email"]
    list_filter = ["name","email"]
    exclude = ["password"]
    class Meta:
        model = Registration
class CommentsAdmin(admin.ModelAdmin):
    list_display = ["name","rating","what_food_comment","comment_created","comment_changed"]
class CuisineAdmin(admin.ModelAdmin):
    list_display = ["id","type_of_cuisine"]
class SessionAdmin(admin.ModelAdmin):
    def _session_data(self, obj):
        return obj.get_decoded()
    list_display = ['session_key', '_session_data', 'expire_date']
class CommentRestaurantAdmin(admin.ModelAdmin):
    list_display = ["name", "rating", "what_restaurant_comment", "comment_created", "comment_changed"]
admin.site.register(Session, SessionAdmin)
admin.site.register(Dish,DishesAdmin)
admin.site.register(Cuisine,CuisineAdmin)
admin.site.register(Meal)
admin.site.register(Unit)
admin.site.register(Currency)
admin.site.register(Comment, CommentsAdmin)
admin.site.register(Registration,CustomersAdmin)
admin.site.register(Restaurant)
admin.site.register(Comment_of_Restaurant,CommentRestaurantAdmin)