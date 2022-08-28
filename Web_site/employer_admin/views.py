from django.shortcuts import render,redirect
from django.views import View
from  django.http import HttpResponse,Http404,HttpResponseRedirect
from survey.forms import FormRegistation,EmployerAdminForm,RestaurantForm,AddProductForm
from .forms import EAdminAuthForm
from survey.models import EmployerAdminAuth, Registration,Restaurant,Dish
import json
import random
import string
from django.core import serializers
import logging
logger = logging.getLogger("django")
def AdminHomePage(request):
    try:
        if (request.session["Check_auth"]==True or request.session["Auth_Check_Admin"]==True):
            data ={
                "name":request.session.get("login")
            }
            logger.debug(data["name"])
            return render(request,"admin/e_admin.html",locals())
        else:
            return redirect("employer_admin:auth")
    except KeyError:
        return redirect("employer_admin:auth")
def AdminProfilePage(request):
    try:
        if (request.session["Check_auth"] == True or request.session["Auth_Check_Admin"]==True):
            admin_data = EmployerAdminAuth.objects.filter(identifier=request.session.get("id"))[0]
            restaurant_data = Restaurant.objects.filter(identifier=request.session.get("id"))[0]
            custom_data = Registration.objects.filter(identifier=request.session.get("id"))[0]
            restaurant_data2 = Restaurant.objects.filter(identifier=request.session.get("id"))
            if request.method == "POST":
                form = FormRegistation(request.POST, instance=custom_data)
                form2 = EmployerAdminForm(request.POST, instance=admin_data)
                form3 = RestaurantForm(request.POST,request.FILES,instance=restaurant_data)
                if form.is_valid() and form2.is_valid() and form3.is_valid():
                                logger.debug(form3.cleaned_data['image_of_restaurant'])
                                form.save()
                                form2.save()
                                form3.save()
                                logger.debug("save")
                else:
                    logger.debug("didn't save")
                    logger.debug(form.errors)
                    logger.debug(form2.errors)
                    logger.debug(form3.errors)
            form = FormRegistation(instance=custom_data)
            form2 = EmployerAdminForm(instance=admin_data)
            form3 = RestaurantForm(instance=restaurant_data)
            data = {
                "form":form,
                "form2":form2,
                "form3":form3,
                "restaurant_data": restaurant_data,
            }
            return render(request,"admin/profile_admin.html",data)
        else:
            return redirect("employer_admin:auth")
    except KeyError:
        return redirect("employer_admin:auth")
def AdminAuthPage(request):
    global name, indefifer
    if request.method == "POST":
        form = EAdminAuthForm(request.POST)
        if EmployerAdminAuth.objects.filter(login=(form["login"].value()).strip(), password_e=(form["password_e"].value()).strip()).exists():
            if form.is_valid():
                data = EmployerAdminAuth.objects.filter(login=(form["login"].value()).strip(), password_e=(form["password_e"].value()).strip())[0]
                request.session["id"] = data.identifier
                request.session["login"] = form["login"].value()
                request.session["Auth_Check_Admin"] = True
                logger.debug(request.session["id"])
                return redirect("employer_admin:home")
        else:
            logger.debug(False)
    try:
        form = EAdminAuthForm(initial={"login":request.session["login"]})
        return render(request,"admin/e_adminform.html",locals())
    except KeyError:
        form = EAdminAuthForm()
        return render(request, "admin/e_adminform.html", locals())
def AdminProductPage(request):
    try:
        if (request.session["Check_auth"] == True or request.session["Auth_Check_Admin"] == True):
            restaurant = Restaurant.objects.filter(identifier=request.session.get("id"))[0]
            name_r = restaurant.id
            products = Dish.objects.filter(names_of_restaurant=name_r,is_active=True)
            return render(request,"add_product_page.html",locals())
        else:
            return redirect("employer_admin:auth")
    except KeyError:
        return redirect("employer_admin:auth")
def AdminProductDetailPage(request):
    try:
        if (request.session["Check_auth"] == True or request.session["Auth_Check_Admin"] == True):
            restaurant = Restaurant.objects.filter(identifier=request.session.get("id"))[0]
            if request.method == "POST":
                form = AddProductForm(request.POST,request.FILES)
                if form.is_valid():
                    num_sybols = 20
                    IN = ''.join(random.choices(string.ascii_uppercase + string.digits, k=num_sybols))
                    form.instance.IN = IN
                    form.instance.names_of_restaurant = restaurant
                    form.save()
                    logger.debug("save")
                    return redirect("employer_admin:product_admin")
            form = AddProductForm()
            data ={
                "form":form,
                "check":True
            }
            return render(request,"add_detail_product.html",data)
        else:
            return redirect("employer_admin:auth")
    except KeyError:
        return redirect("employer_admin:auth")
def AdminChangeProductDetailPage(request,pk):
    try:
        if (request.session["Check_auth"] == True or request.session["Auth_Check_Admin"] == True):
            product_exist = Dish.objects.filter(id=pk).exists()
            if product_exist == True:
                product = Dish.objects.get(id=pk)
                if request.method == "POST":
                    form = AddProductForm(request.POST,request.FILES,instance=product)
                    if form.is_valid():
                        form.save()
                        return redirect("employer_admin:product_admin")
                elif request.method == "DELETE":
                    logger.debug(request.method)
                    Dish.objects.get(id=pk).delete()
                    return redirect("employer_admin:product_admin")
                form = AddProductForm(instance=product)
                data = {
                    "form": form,
                    "check": False
                }
                return render(request, "add_detail_product.html",data)
            else:
                return redirect("employer_admin:product_admin")
        else:
            return redirect("employer_admin:auth")
    except KeyError:
        return redirect("employer_admin:auth")
def AdminOrderPage(request):
    try:
        if (request.session["Check_auth"] == True or request.session["Auth_Check_Admin"] == True):
            return render(request, "admin/orders_restaraunt.html")
        else:
            return redirect("employer_admin:auth")
    except KeyError:
        return redirect("employer_admin:auth")