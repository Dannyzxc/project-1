from django.db import models
# from datetime import date,datetime

# Create your models here.
class contact(models.Model):
    username = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    phone = models.CharField(max_length=150)
    description = models.TextField(max_length=550)
    date = models.DateField()
 
    def __str__(self):
        return self.username 
 
 
class products(models.Model):
    category = models.CharField(max_length=50, default="")
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    price = models.IntegerField(default="100")
    image = models.ImageField(upload_to="shop/images", default="")

    def __str__(self):
        return self.product_name

class profile(models.Model):
    username = models.CharField(max_length=50,default="")
    email = models.CharField(max_length=100,default="")
    address = models.CharField(max_length=200,default="")
    # date = models.DateField(("Date"), default=datetime.date.today())
    # (_("Date"), auto_now_add=True)
    
    def __str__(self):
        return self.username