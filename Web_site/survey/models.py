from django.db import models
from django.utils.safestring import mark_safe
class Registration(models.Model):
    identifier = models.CharField(default="",max_length=200)
    name = models.CharField(default="",blank=True,null=True,max_length=50)
    email = models.EmailField(max_length=100)
    password_r = models.CharField(default="",max_length=50)
    courier = models.BooleanField(default=False)
    customer = models.BooleanField(default=False)
    employer = models.BooleanField(default=False)
class Cuisine(models.Model):
    type_of_cuisine = models.CharField(default="",max_length=210)
    def __str__(self):
        return self.type_of_cuisine
class Meal(models.Model):
    type_of_meal = models.CharField(max_length=210)
    def __str__(self):
        return self.type_of_meal
class Currency(models.Model):
    currency = models.CharField(default="",max_length=50)
    def __str__(self):
        return self.currency
class Unit(models.Model):
    unit = models.CharField(max_length=50)
    def __str__(self):
        return self.unit
class Restaurant(models.Model):
    identifier = models.CharField(default="", max_length=200)
    image_of_restaurant = models.ImageField(upload_to='ckeditor',blank=True,null=True)
    restaurant_name = models.CharField(default="",blank=True,null = True,max_length=100)
    rating = models.IntegerField(default=0,blank=True)
    type_of_cuisine = models.ForeignKey(Cuisine,blank=True,null=True,on_delete=models.CASCADE)
    description = models.TextField(default="",blank=True)
    lat = models.FloatField(default=0,blank=True)
    lng = models.FloatField(default=0,blank=True)
    address_of_restaurant = models.CharField(default="", max_length=1000,blank=True)
    def __str__(self):
        return self.restaurant_name
class Dish(models.Model):
    IN = models.CharField(default="", max_length=200)
    name = models.CharField(max_length=100)
    rating = models.IntegerField(default=0)
    price = models.IntegerField()
    currency = models.ForeignKey(Currency,on_delete=models.CASCADE)
    mass_of_meal = models.IntegerField()
    unit_of_measurement = models.ForeignKey(Unit,on_delete=models.CASCADE)
    image_of_meal = models.ImageField(upload_to='ckeditor')
    type_of_meal = models.ForeignKey(Meal,on_delete=models.CASCADE)
    names_of_restaurant = models.ForeignKey(Restaurant,on_delete=models.CASCADE)
    consist = models.TextField(blank=True)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.name
class Comment(models.Model):
    name = models.CharField(max_length=100)
    title= models.CharField(default="",max_length=20)
    rating = models.IntegerField(default=0)
    what_food_comment = models.ForeignKey(Dish, on_delete=models.CASCADE)
    comment = models.TextField()
    comment_created = models.DateTimeField(auto_now_add=True,auto_now=False)
    comment_changed = models.DateTimeField(auto_now_add=False, auto_now=True)
class Comment_of_Restaurant(models.Model):
    name = models.CharField(max_length=100)
    title= models.CharField(default="",max_length=20)
    rating = models.IntegerField(default=0)
    what_restaurant_comment = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    comment = models.TextField()
    comment_created = models.DateTimeField(auto_now_add=True,auto_now=False)
    comment_changed = models.DateTimeField(auto_now_add=False, auto_now=True)
class EmployerAdminAuth(models.Model):
    identifier = models.CharField(default="", max_length=200)
    login = models.CharField(default="",blank=True,null=True,max_length=100)
    password_e = models.CharField(default="",max_length=50)
class Basket(models.Model):
    id_order = models.CharField(default="", max_length=200)
    id_product = models.CharField(default="", max_length=200)
    id_customer = models.CharField(default="", max_length=200)
    id_session = models.CharField(default="", max_length=200)
    name_of_dish = models.CharField(default="", max_length=100)
    price = models.IntegerField(default=0)
    currency = models.ForeignKey(Currency,null=True,on_delete=models.CASCADE)
    col = models.PositiveBigIntegerField(default=0)
    add_product_at_basket = models.DateTimeField(auto_now_add=True, auto_now=False)
    auth = models.BooleanField(default=False)
    image_of_meal = models.ImageField(default="",upload_to='ckeditor')
    price_for_one = models.IntegerField(default=0)
class Order(models.Model):
    id_order = models.CharField(default="", max_length=200)
    id_product = models.CharField(default="", max_length=200)
    id_customer = models.CharField(default="", max_length=200)
    name_of_dish = models.CharField(default="", max_length=100)
    price = models.IntegerField(default=0)
    currency = models.ForeignKey(Currency, null=True, on_delete=models.CASCADE)
    col = models.PositiveBigIntegerField(default=0)
    image_of_meal = models.ImageField(default="", upload_to='ckeditor')
    price_for_one = models.IntegerField(default=0)