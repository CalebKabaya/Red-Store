from django.contrib import admin
from .models import User,Customer,Client

# Register your models here.
admin.site.register(User)
admin.site.register(Client)
admin.site.register(Customer)
