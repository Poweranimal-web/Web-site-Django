from django.forms import ModelForm, TextInput,PasswordInput,CheckboxInput,Textarea,FileInput,NumberInput
from django import forms
from .models import Registration, Comment, EmployerAdminAuth, Restaurant, Cuisine,Dish,Currency,Unit,Meal,Comment_of_Restaurant
from django.utils.translation import gettext_lazy as _
class RegRestaurantForm(ModelForm):
    class Meta:
        model = Restaurant
        field = ["restaurant_name"]
        exclude = ['identifier',"image_of_restaurant","type_of_cuisine","description","type_of_cuisine"]
        widgets = {
            "restaurant_name": TextInput(attrs={
                "class": "name_r",
                "placeholder": "Название ресторана",
                "type": "text",
                "id": "r_name",
                "name": "r_name",
            }),
        }
class FormRegistation(ModelForm):
    class Meta:
        model = Registration
        fields = ['name','password_r','email']
        exclude = ['identifier','courier','customer','employer']
        widgets = {
            "name": TextInput(attrs={
                "class": "name",
                "placeholder": "Имя",
                "type": "text",
                "id": "name",
                "name": "name"
            }),
            "password_r": PasswordInput(render_value = True,attrs={
                "class": "password",
                "placeholder": "Пароль",
                "type": "password",
                "id": "password"
            }),
            "email": TextInput(attrs={
                "class": "email",
                "placeholder": "Email",
                "type": "text",
            }),
            "courier": CheckboxInput(attrs={
                "class": "courier"
            }),
            "customer": CheckboxInput(attrs={
                "class": "customer"
            }),
            "employer": CheckboxInput(attrs={
                "class": "employer"
            }),
        }
class FormRegistation2(ModelForm):
    class Meta:
        model = Registration
        fields = ['name', 'password_r', 'email', 'courier', 'customer', 'employer']
        exclude = ['identifier']
        widgets = {
            "name": TextInput(attrs={
                "class": "name",
                "placeholder": "Имя",
                "type": "text",
                "name": "name",
                "id": "name",
            }),
            "password_r": PasswordInput(render_value=True, attrs={
                "class": "password",
                "placeholder": "Пароль",
                "type": "password",
                "id": "password",
                "name":"password",
            }),
            "email": TextInput(attrs={
                "class": "email",
                "placeholder": "Email",
                "type": "text",
                "name": "email",
                "id": "email"
            }),
            "courier": CheckboxInput(attrs={
                "class": "courier",
                "id": "courier"

            }),
            "customer": CheckboxInput(attrs={
                "class": "customer",
                "id": "customer"
            }),
            "employer": CheckboxInput(attrs={
                "class": "employer",
                "id": "employer"
            })
        }
class RepeatForm(forms.Form):
        repeat_password = forms.CharField(max_length=40, widget=TextInput(attrs={
        "placeholder": "Повторите пароль",
        "type": "password",
        "class": "r_password",
        "id":"r_password"
        }))
class VeficateCodeForm(forms.Form):
    code = forms.CharField(max_length=6, widget=TextInput(attrs={
        "placeholder": "Введите код",
        "type": "text",
        "class": "code",
        "text-transform": "uppercase"
        }))
class CommentForm(ModelForm):
    class Meta:
        model = Comment
        field =["name","title","comment"]
        exclude = ["rating","what_food_comment","comment_created","comment_changed"]
        widgets = {
            "name": TextInput(attrs={
                "class":"name",
                "placeholder": "Имя",
                "type": "text",
            }),
            "title": TextInput(attrs={
                "class": "title",
                "placeholder": "Заголовок",
                "type": "text",
            }),
            "comment": TextInput(attrs={
                "class": "comment",
                "placeholder": "Коментарий",
                "type": "text",
            }),
        }
class CommentFormRestaraunt(ModelForm):
    class Meta:
        model = Comment_of_Restaurant
        field =["name","title","comment"]
        exclude = ["rating","what_restaurant_comment","comment_created","comment_changed"]
        widgets = {
            "name": TextInput(attrs={
                "class":"name",
                "placeholder": "Имя",
                "type": "text",
            }),
            "title": TextInput(attrs={
                "class": "title",
                "placeholder": "Заголовок",
                "type": "text",
            }),
            "comment": TextInput(attrs={
                "class": "comment",
                "placeholder": "Коментарий",
                "type": "text",
            }),
        }
class EmployerAdminForm(ModelForm):
    class Meta:
        model = EmployerAdminAuth
        field = ["login","password_e"]
        exclude = ['identifier']
        widgets = {
            "login": TextInput(attrs={
                "class": "ename",
                "placeholder": "Имя",
                "type": "text",
                "id": "e_name",
                "name":"e_name"
            }),
            "password_e": PasswordInput(render_value = True,attrs={
                "class": "epassword",
                "placeholder": "Пароль",
                "type": "password",
                "id": "e_password",
                "name": "e_password"
            }),
        }
class RestaurantForm(ModelForm):
    class Meta:
        model = Restaurant
        field = ["image_of_restaurant","restaurant_name","type_of_cuisine","description"]
        exclude = ['identifier']
        widgets = {
            "restaurant_name": TextInput(attrs={
                "class": "name_r",
                "placeholder": "Название",
                "type": "text",
                "id": "r_name",
                "name": "r_name",
            }),
            "description": Textarea(attrs={
                "class": "description_r",
                "placeholder": "Описания",
            }),
            "image_of_restaurant": FileInput(attrs={
                "class": "image_r",
            }),
        }

    def __init__(self, *args, **kwargs):
        super(RestaurantForm, self).__init__(*args, **kwargs)
        self.fields['type_of_cuisine'] = forms.ModelChoiceField(queryset=Cuisine.objects.all(),widget=forms.Select(attrs={
            "id": "type_of_cuisine",
            "name": "type_of_cuisine"
        }))
class AddProductForm(ModelForm):
    class Meta:
        model = Dish
        field = ["name", "price","currency","image_of_meal", "mass_of_meal",'unit_of_measurement',"type_of_meal","consist","description","is_active"]
        exclude = ["IN","rating","names_of_restaurant"]
        widgets ={
            "name":TextInput(attrs={
                "class":"name",
                "placeholder": "Название блюда",
                "type": "text",
            }),
            "price":NumberInput(attrs={
                "class": "price",
                "placeholder": "Цена",
                "type": "number",
            }),
            "mass_of_meal":NumberInput(attrs={
                "class": "mass",
                "placeholder": "Масса",
                "type": "number",
            }),
            "consist":Textarea(attrs={
                "class": "consist",
            }),
            "description": Textarea(attrs={
                "class": "description",
            }),
            "image_of_meal": FileInput(attrs={
                "class":"image_of_meal"
            }),
            "is_active": CheckboxInput(attrs={
                "class": "is_active"
            })
        }
    def __init__(self, *args, **kwargs):
        super(AddProductForm, self).__init__(*args, **kwargs)
        self.fields['currency'] = forms.ModelChoiceField(queryset=Currency.objects.all(),widget=forms.Select(attrs={
            "class": "currency"
        }))
        self.fields['unit_of_measurement'] = forms.ModelChoiceField(queryset=Unit.objects.all(),widget=forms.Select(attrs={
            "class": "unit_of_measurement"
        }))
        self.fields['type_of_meal'] = forms.ModelChoiceField(queryset=Meal.objects.all(),widget=forms.Select(attrs={
            "class": "type_of_meal"
        }))