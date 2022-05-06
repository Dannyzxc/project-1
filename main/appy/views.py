from email.headerregistry import Address
from django.shortcuts import render,HttpResponse
from datetime import  datetime
from .models import contact,products,profile
from django.contrib import messages
from math import ceil
# import logging
import json 
 

def index(request):
    all_products = []
    categories_of_products = products.objects.values('category','id')
    all_categories = {item['category'] for item in categories_of_products}
    for thing in all_categories:
        filtered_products = products.objects.filter(category=thing)
        n = len(filtered_products)
        n_slides = n // 4 + ceil((n/4) - ( n// 4))
        all_products.append([filtered_products, range(1,n_slides),n_slides])
    my_dict = {'all_products':all_products}
    return render(request, "index.html",my_dict)

def about(request):
    return render(request,'about.html')
    # return HttpResponse('this is the about page')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        description = request.POST.get('desc')
        # date = request.POST.get('name')
        Contact = contact(name=name, email=email, phone=phone, desc=description, date=datetime.today())
        Contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request, 'contact.html')
    # return HttpResponse('this is the contact page')

def profiles(request):
    if request.method == "POST":
        username = request.POST.get('name')
        email = request.POST.get('email')
        Address = request.POST.get('address')
        Profile = profile(username=username,email=email,address=Address)
        Profile.save()
        messages.success(request, 'Your profile has been saved')
        
    my_users = profile.objects.values()
    return render(request,'profile.html',{'my_users':my_users})


