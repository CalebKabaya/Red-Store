from rest_framework import serializers
# from ..models import User,Client,Customer
from ..models import *
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()





class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','email','is_client']


# class CustomerSignupSerializers(serializers.ModelSerializer):
#     class Meta:
#         password=serializers.CharField(style={"input_type":"password"},write_only=True)
#         password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

#         model=User
#         fields=['username','email','password','password2']
      

#     def save(self, **kwargs):
#         user=User(
#             username=self.validated_data['username'],
#             email=self.validated_data['email']
#         )
#         password=self.validated_data['password'],
#         password2=self.validated_data['password2']
#         if password !=password2:
#             raise serializers.ValidationError({"error":"password do not match"})
#         user.set_password(password)

#         user.is_customer=True
#         user.save()
#         Customer.objects.create(user=user)

#         return user 


# class ClientSignupSerializers(serializers.ModelSerializer):
#     class Meta:
#         password=serializers.CharField(style={"input_type":"password"},write_only=True)
#         password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

#         model=User
#         fields=['username','email','password','password2']
       

#     def save(self, **kwargs):
#         user=User(
#             username=self.validated_data['username'],
#             email=self.validated_data['email']
#         )
#         password=self.validated_data['password'],
#         password2=self.validated_data['password2']
#         if password !=password2:
#             raise serializers.ValidationError({"error":"password do not match"})
#         user.set_password(password)
#         user.is_client=True
#         user.save()
#         Client.objects.create(user=user)

#         return user

       
class CustomerSignupSerializers(serializers.ModelSerializer):
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
      

    def save(self, **kwargs):
        user = User(
            username=self.validated_data['username'],
            email=self.validated_data['email']
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'error': 'password do not match'})
        user.set_password(password)
        user.is_customer = True
        user.save()
        Customer.objects.create(user=user)
        return user

 
class ClientSignupSerializers(serializers.ModelSerializer):
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
       

    def save(self, **kwargs):
        user = User(
            username=self.validated_data['username'],
            email=self.validated_data['email']
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'error': 'password do not match'})
        user.set_password(password)
        user.is_client = True
        user.save()
        Client.objects.create(user=user)
        return user   