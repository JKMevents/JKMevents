
from django.db import models
from django.contrib.auth.models import User

    
class User_information(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=254, default="default_username")
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length = 30)
    email = models.EmailField(max_length=254)
    phone = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.first_name
    

class TicketCounter(models.Model):
    #user = models.ForeignKey(User_information, on_delete=models.CASCADE)
    count = models.IntegerField(default=0)

class Tickets(models.Model):
    user = models.ForeignKey(User_information, on_delete=models.CASCADE)
    count = models.IntegerField(default=0)
