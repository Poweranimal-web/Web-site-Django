from django.urls import path
from . import views
app_name = "employer_admin"
urlpatterns = [
    path("",views.AdminHomePage, name="home"),
    path("profile/",views.AdminProfilePage, name="profile"),
    path("auth/",views.AdminAuthPage),
    path("product_admin/", views.AdminProductPage, name="product_admin"),
    path("product_admin/detail/",views.AdminProductDetailPage, name="product_detail"),
    path("product_admin/detail/<int:pk>",views.AdminChangeProductDetailPage, name="product_change"),
    path("product_admin/orders/",views.AdminOrderPage, name="order")
]