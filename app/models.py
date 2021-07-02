
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

# Create your models here.

class Customer(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=30,null=True, blank=True, default=None)
	address = models.CharField(max_length=250,null=True, blank=True, default=None)
	email = models.EmailField(max_length=250,blank=True, null= True, unique= True)
	# phone = models.IntegerField()
	phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
	phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list
	def __str__(self):
		return self.name
class Order(models.Model):
	order_id = models.AutoField(primary_key=True)
	customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
	item = models.CharField(max_length=250,null=True, blank=True, default=None)
	price = models.FloatField(null=True, blank=True, default=None)

	def __str__(self):
		return self.item
