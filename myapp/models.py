from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save
from django.conf import settings
from django.dispatch import receiver

# Create your models here.
class User(AbstractUser):
    is_customer=models.BooleanField(default=False)
    is_client=models.BooleanField(default=False)



    def __str__(self):
        return self.username
@receiver(post_save,sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None,created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)



class Customer(models.Model):
    user=models.OneToOneField(User,related_name="customer",on_delete=models.CASCADE)
    email=models.CharField(max_length=120)
    phone=models.CharField(max_length=120)


    def __str__(self):
        return self.username



class Client(models.Model):
    user=models.OneToOneField(User,related_name="client",on_delete=models.CASCADE)
    email=models.CharField(max_length=120)
    phone=models.CharField(max_length=120)


    def __str__(self):
        return self.username









