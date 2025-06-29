from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

CATEGORY_CHOICES=[
    ('Food','Food'),
    ('Clothes','Clothes'),
    ('Books','Books'),
    ('Toys','Toys'),
    ('Sanitary Kits','Sanitary Kits')
]

class Donation(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    category= models.CharField(max_length=50,choices=CATEGORY_CHOICES)
    item_description = models.TextField()
    quantity= models.PositiveIntegerField()
    donated_on= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.category}"
    

class Contact(models.Model):
    name = models.CharField(max_length=50)    
    email = models.EmailField()
    phone_number =PhoneNumberField(blank=True)
    subject = models.TextField()
    message= models.TextField(max_length=200)
    consent=models.BooleanField(default=False,help_text="I agree to the privacy policy")

    def __str__(self):
        return f"{self.name}-{self.subject[:30]}"