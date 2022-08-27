from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from  django.http import HttpResponse,Http404,HttpResponseRedirect,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from  .models import Registration,Dish,Currency,Comment,EmployerAdminAuth,Restaurant, Basket,Comment_of_Restaurant,Order
from django.core.mail import send_mail
from django.views.generic.list import ListView
from django.shortcuts import render,redirect,reverse
from .forms import FormRegistation, RepeatForm, VeficateCodeForm,CommentForm,FormRegistation2, RegRestaurantForm, CommentFormRestaraunt
from django.core.paginator import Paginator
import string
import random
import smtplib
import json
import namegenerator
from liqpay import LiqPay
from django.core import serializers
import logging
admin_login = str()
admin_password = str()
email = str()
name = str()
Check_auth = False
mapbox_access_token = str('pk.eyJ1IjoicG93ZXJhbmltYWwyMDIyIiwiYSI6ImNsNDN2ZWRycDFsZnozYnF5cDcwMTdxYnMifQ.wyc73X1ViS_L2Je4tn0aRQ')
logger = logging.getLogger('django')
def RendHomepage(request):
    global name,Check_auth
    restaraunts = Restaurant.objects.all()
    currency = Currency.objects.filter(currency="UA")
    id_session = ''.join(random.choices(string.ascii_uppercase + string.digits, k=20))
    if request.method == "DELETE":
        data = json.loads(request.body.decode("utf-8"))
        if data["set"] == "sign_out":
            del request.session["name"]
            del request.session["Check_auth"]
            del request.session["id"]
            del request.session["email"]
            del request.session["Auth_Check_Admin"]
            template = render(request, "home.html", locals())
            template.set_cookie("auth", False, httponly=False)
    try:
        if request.session["Check_auth"] == True:
            logger.debug(request.session["Check_auth"])
            data = {
                "name":request.session["name"],
                "auth":request.session["Check_auth"]
            }
            template = render(request, "home.html", locals())
            if (request.COOKIES.get('id_session')):
                template.set_cookie("auth", request.session["Check_auth"], httponly=False)
            else:
                template.set_cookie("auth", request.session["Check_auth"], httponly=False)
                template.set_cookie("id_session", id_session, max_age=86400, httponly=False)
        else:
            logger.debug(request.session["Check_auth"])
            data = {
                "name": None,
                "auth": request.session["Check_auth"]
            }
            template = render(request, "home.html", locals())
            if (request.COOKIES.get('id_session')):
                template.set_cookie("auth", request.session["Check_auth"], httponly=False)
            else:
                template.set_cookie("auth", request.session["Check_auth"], httponly=False)
                template.set_cookie("id_session", id_session, max_age=86400, httponly=False)
    except KeyError:
        request.session["Check_auth"] = False
        print(request.session["Check_auth"])
        data = {
            "name": None,
            "auth": request.session["Check_auth"]
        }
        template = render(request, "home.html", locals())
        if (request.COOKIES.get('id_session')):
            template.set_cookie("auth",request.session["Check_auth"] , httponly=False)
        else:
            template.set_cookie("auth",request.session["Check_auth"] , httponly=False)
            template.set_cookie("id_session",id_session,max_age=86400,httponly=False)
    return template
def RendRegpage(request):
    global name, email,admin_login,admin_password
    if request.method == "POST":
        if request.POST.get('status') == "restaurant":
            if request.POST["password"] == request.POST["repeat_password"]:
                request.session["name"] = request.POST["first_name"]
                request.session["email"] = request.POST["email"]
                email = request.POST["email"]
                name = request.POST["first_name"]
                if request.POST["employer"] == "true":
                    S = 20
                    lower = string.ascii_lowercase
                    upper = string.ascii_uppercase
                    num = string.digits
                    symbols = string.punctuation
                    all = lower + upper + num + symbols
                    temp = random.sample(all, 20)
                    password = "".join(temp)
                    ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k=S))
                    login = namegenerator.gen()
                    admin_login = login
                    admin_password = password
                    employer_admin_account = EmployerAdminAuth(identifier=ran,login=login,password_e=password)
                    identifier_restaurant = Restaurant(identifier=ran, restaurant_name=request.POST["name_of_restaurant"],address_of_restaurant=request.POST["address"],lat=request.POST["lat"],lng=request.POST["lng"])
                    account = Registration(identifier=ran,name=request.POST["first_name"],email=request.POST["email"],password_r=request.POST["password"],employer=True)
                    request.session["id"] = ran
                    account.save()
                    employer_admin_account.save()
                    identifier_restaurant.save()
            else:
                logger.debug("unvalid")
        else:
            form = FormRegistation2(request.POST)
            form2 = RepeatForm(request.POST)
            if form["password_r"].value() == form2["repeat_password"].value():
                request.session["name"] = form["name"].value()
                request.session["email"] = form["email"].value()
                email = form["email"].value()
                name = form["name"].value()
                if form.is_valid():
                        S = 20
                        ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k=S))
                        request.session["id"] = ran
                        form.instance.identifier = ran
                        form.save()
                        return redirect("survey:code")
            else:
                logger.debug("unvalid")
    user= {
        "name": str(),
        "password": str(),
        "email": str(),
    }
    form = FormRegistation2()
    form2 = RepeatForm()
    form3 = RegRestaurantForm()
    return render(request,"form.html",locals())
def RendNoticePage(request):
    if request.method == "GET":
        request.session["Check_auth"] = True
        request.session["Auth_Check_Admin"] = True
        SendAdminEmail()
    return render(request, "notice.html")
def RendClientCodeForm(request):
    global Check_auth
    if request.method == "GET":
        code = sendEmail(request.session["email"],request.session["name"])
        request.session["code"] = code
    if request.method == "POST":
        form = VeficateCodeForm(request.POST)
        if (form["code"].value()).upper() == request.session["code"]:
            request.session["Check_auth"] = True
            request.session["Auth_Check_Admin"] = True
            return redirect("survey:home")
    form = VeficateCodeForm()
    data = {
            "form": form
    }
    return render(request, "email_verficate.html", data)
def RendResturauntPage(request,pk):
    restaraunt = Restaurant.objects.get(id=pk)
    dishes = Dish.objects.filter(names_of_restaurant=restaraunt,is_active=True)
    comments = Comment_of_Restaurant.objects.filter(what_restaurant_comment=restaraunt)
    form = CommentFormRestaraunt()
    template = render(request, "restaurant_page.html", locals())
    if request.method == "POST":
        if request.POST.get("status") == "add_product":
            try:
                auth_check = Registration.objects.filter(name=request.session["name"], email=request.session["email"]).exists()
                if auth_check == True:
                        auth = Registration.objects.filter(name=request.session["name"],email=request.session["email"])[0]
                        basket_check = Basket.objects.filter(id_session=request.COOKIES.get('id_session')).exists()
                        if basket_check == True:
                            basket_meal_check = Basket.objects.filter(id_session=request.COOKIES.get('id_session'),id_product=request.POST["IN"]).exists()
                            if basket_meal_check == True:
                                basket_meal = Basket.objects.filter(id_session=request.COOKIES.get('id_session'),id_product=request.POST["IN"])[0]
                                new_number = int(basket_meal.col)+1
                                new_price = int(basket_meal.price_for_one)*new_number
                                basket = Basket.objects.filter(id_session=request.COOKIES.get('id_session'),id_product=request.POST["IN"]).update(col=new_number,price=new_price)
                                template.set_cookie("number_meal_basket", int(request.COOKIES.get("number_meal_basket")) + 1, max_age=86400, httponly=False)
                                return template
                            else:
                                info_meal = Dish.objects.filter(IN=request.POST["IN"])[0]
                                basket, created = Basket.objects.get_or_create(image_of_meal=info_meal.image_of_meal,name_of_dish=info_meal.name,price=info_meal.price,currency=info_meal.currency,id_session=request.COOKIES.get('id_session'),id_product=request.POST["IN"],col=1,price_for_one=int(info_meal.price))
                                template.set_cookie("number_meal_basket", int(request.COOKIES.get("number_meal_basket")) + 1, max_age=86400, httponly=False)
                                return template
                        else:
                            info_meal = Dish.objects.filter(IN=request.POST["IN"])[0]
                            basket, created = Basket.objects.get_or_create(image_of_meal=info_meal.image_of_meal,name_of_dish=info_meal.name,price=info_meal.price,currency=info_meal.currency,id_session=request.COOKIES.get('id_session'),id_product=request.POST["IN"],col=1,price_for_one=int(info_meal.price))
                            template.set_cookie("number_meal_basket", int(request.COOKIES.get("number_meal_basket")) + 1, max_age=86400, httponly=False)
                            return template
                else:
                    return redirect("survey:auth")
            except KeyError:
                return redirect("survey:auth")
        elif request.POST.get("status")=="add_rating":
            logger.debug(request.POST.get("rating"))
        else:
            form = CommentFormRestaraunt(request.POST)
            if form.is_valid():
                form.instance.what_restaurant_comment = restaraunt
                form.save()
                return HttpResponseRedirect(request.path)
    if (request.COOKIES.get("number_meal_basket")):
        pass
    else:
        template.set_cookie("number_meal_basket",0,max_age=86400,httponly=False)
    return template
def RendClientAuthForm(request):
    if request.method == "POST":
        form = FormRegistation(request.POST)
        check = Registration.objects.filter(name=form["name"].value() ,email=form["email"].value(),password_r=form["password_r"].value()).exists()
        logger.debug(form["name"].value())
        logger.debug(form["email"].value())
        logger.debug(form["password_r"].value())
        if check == True:
            request.session["name"] = form["name"].value()
            request.session["email"] = form["email"].value()
            data = Registration.objects.filter(name=form["name"].value(), email=form["email"].value(),password_r=form["password_r"].value())[0]
            request.session["id"] = data.identifier
            return redirect("survey:code")
        else:
            logger.debug(False)
    form = FormRegistation()
    data={
       "form": form
    }
    return render(request, "form2.html", data)
def RendProductPage(request,pk):
        product = Dish.objects.get(id=pk)
        if request.method == "POST":
            form = CommentForm(request.POST)
            if form.is_valid():
                form.instance.what_food_comment = product
                form.save()
                return HttpResponseRedirect(request.path)
        comments = Comment.objects.filter(what_food_comment=product)
        currency = Currency.objects.filter(currency="UA")
        form = CommentForm()
        return render(request, "eat_page.html", locals())
def PaginationProductPage(request,cuisine):
    if request.method == "GET":
        restaurants = Restaurant.objects.filter(type_of_cuisine__type_of_cuisine=cuisine)
        paginator = Paginator(restaurants, 1)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request,"pagination.html",locals())
def PaymentPage(request):
        liqpay = LiqPay("sandbox_i52254063589", "sandbox_mncjsVVGsxkuFNNSNAJr08U2tRm8Aku4sEBTqHi7")
        params = {
            'action': 'pay',
            'amount': request.COOKIES.get("amount"),
            'currency': 'UAH',
            'description': 'Buyah.com products',
            'order_id': ''.join(random.choices(string.ascii_uppercase + string.digits, k=6)),
            'version': '3',
            'sandbox': 0,  # sandbox mode, set to 1 to enable it
            'server_url': 'https://test.com/billing/pay-callback/',  # url to callback view
        }
        signature = liqpay.cnb_signature(params)
        data = liqpay.cnb_data(params)
        template = render(request, "payment.html", {'signature': signature, 'data': data})
        id_session = ''.join(random.choices(string.ascii_uppercase + string.digits, k=20))
        if request.method == "POST":
            baskets = Basket.objects.filter(id_session=request.COOKIES.get('id_session')).values()
            logger.debug(baskets)
            for basket in baskets:
                order = Order(id_order=basket["id_session"],id_product=basket["id_product"],name_of_dish=basket["name_of_dish"],price=basket["price"],col=basket["col"],image_of_meal=basket["image_of_meal"],price_for_one=basket["price_for_one"])
                order.save()
            Basket.objects.filter(id_session=request.COOKIES.get('id_session')).delete()
            logger.debug(request.COOKIES.get('id_session'))
            template.set_cookie("id_session",id_session,max_age=86400, httponly=False)
            template.set_cookie("number_meal_basket", 0, max_age=86400, httponly=False)
        return template
def BasketPage(request):
    products = Basket.objects.filter(id_session=request.COOKIES.get("id_session"))
    basket = list(Basket.objects.filter(id_session=request.COOKIES.get('id_session')).values("price"))
    total_price = int()
    for value in basket:
        total_price += int(value["price"])
    data = {"total_price": total_price,
            "currency": "UA"
            }
    template = render(request, "basket.html",locals())
    if request.method == "POST":
        if request.POST["status"]=="increase":
            dish = Dish.objects.filter(IN=request.POST["IN"])[0]
            basket = Basket.objects.filter(id_session=request.COOKIES.get('id_session'),id_product=request.POST["IN"])[0]
            Basket.objects.filter(id_session=request.COOKIES.get('id_session'),id_product=request.POST["IN"]).update(col=int(basket.col)+1,price=dish.price*(int(basket.col)+1))
        elif request.POST["status"]=="reduce":
            basket = Basket.objects.filter(id_session=request.COOKIES.get('id_session'), id_product=request.POST["IN"])[0]
            dish = Dish.objects.filter(IN=request.POST["IN"])[0]
            if int(basket.col) <=0:
                Basket.objects.filter(id_session=request.COOKIES.get('id_session'),id_product=request.POST["IN"]).update(col=0,price=dish.price*0)
            else:
                Basket.objects.filter(id_session=request.COOKIES.get('id_session'), id_product=request.POST["IN"]).update(col=int(basket.col)-1,price=dish.price*(int(basket.col)-1))
    elif request.method == "DELETE":
        data_from_delete = json.loads(request.body.decode("utf-8"))
        logger.debug(data_from_delete)
        Basket.objects.filter(id_product=data_from_delete["IN"],id_session=request.COOKIES.get('id_session')).delete()
    return template
def SettingsPage(request):
    custom_data = Registration.objects.filter(identifier=request.session.get("id"))[0]
    form = FormRegistation(instance=custom_data)
    template = render(request, "settings.html", locals())
    if request.method == "POST":
        form = FormRegistation(request.POST,instance=custom_data)
        if form.is_valid():
            form.save()
            logger.debug("save")
    elif request.method == "DELETE":
        data = json.loads(request.body.decode("utf-8"))
        if data["set"] == "delete_account":
            del request.session["name"]
            del request.session["Check_auth"]
            template.set_cookie("auth", False, httponly=False)
            Registration.objects.filter(identifier=request.session.get("id")).delete()
    return template
def maps(request):
    if request.method == "POST":
        Restaurant.objects.filter(identifier=request.session.get("id")).update(address_of_restaurant=request.POST["address"],lat=request.POST["lat"],lng=request.POST["lng"])
    return render(request, 'indicate_restaraunt.html', {'mapbox_access_token': mapbox_access_token})
def sendEmail(email,name):
    S = 6  # number of characters in the string.
    # call random.choices() string module to find the string in Uppercase + numeric data.
    ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k=S))
    code = ran
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('buyahh11@gmail.com', 'shdjnaonlixhfgfz')

    try:
        server.sendmail('buyahh11@gmail.com',email,              'Hi %s,'
                                                                 'We are happy you signed up.To start exploring,please confirm your email address.'
                                                                 'Your code is %s.' % (name, code))
    except:
        logger.debug('An error occurred when trying to send an email')

    server.quit()
    return code
def SendAdminEmail():
    global name, email,admin_login,admin_password
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('buyahh11@gmail.com', 'shdjnaonlixhfgfz')
    server.sendmail('buyahh11@gmail.com',email,  "Hi %s,\nWe are happy you signed up.\nLink:https://buyah.com/e_admin/auth.\nYour password is %s and login %s" % (name,admin_password, admin_login))
    admin_password = str()
    admin_login = str()
    server.quit()

