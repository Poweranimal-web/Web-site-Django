from  django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name = 'survey'
urlpatterns = [
    path("",views.RendHomepage, name="home"),
    path("reg/",views.RendRegpage, name="reg"),
    path("cousin/<str:cuisine>/",views.PaginationProductPage, name="pag"),
    path("reg/1/code/", views.RendClientCodeForm, name="code"),
    path("auth/",views.RendClientAuthForm, name="auth"),
    path('product/<int:pk>/',views.RendProductPage, name="product"),
    path("reg/notice/", views.RendNoticePage,name="notice"),
    path("restaurant/<int:pk>/", views.RendResturauntPage ,name="restaraunt"),
    path("basket/",views.BasketPage,name="basket"),
    path('pay/', views.PaymentPage, name='pay_view'),
    path('settings/', views.SettingsPage, name='settings'),
    path('map/', views.maps, name='map'),

]

