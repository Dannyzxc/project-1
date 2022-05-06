from django.contrib import admin
from django.urls import path,include
from . import views



urlpatterns = [
    path('',views.index,name="home"),
    path('about/',views.about,name="about"),
    path('contact/',views.contact,name="contact"),
    path('profile/',views.profiles,name="profile"),

    # path("Checkout/", views.checkouts, name="Checkout forms"),
    # path("Payment/", views.Payment, name="Payment forms"),
    path("Products/<int:my_id>", views.products, name="shop Products"),

]

 