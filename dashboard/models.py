from django.db import models
from django.contrib.auth.models import User
CATEGORY=(
        ("Stationary","Stationary"),
        ("Food","Food"),
        ("Electronics","Electronics")
    )
class Meta:
    verbose_name_plural="Product"

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=100,null=True)
    category=models.CharField(max_length=100,choices=CATEGORY,null=True)
    quantity=models.PositiveIntegerField(null=True)

    
    def __str__(self):
        return self.name
    
class Order(models.Model):
    product=models.ForeignKey(Product,models.CASCADE,null=True)
    staff=models.ForeignKey(User,models.CASCADE,null=True)  
    quantity=models.PositiveIntegerField(null=True)
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product} ordered by {self.staff}"  

