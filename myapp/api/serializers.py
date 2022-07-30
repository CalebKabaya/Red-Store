from rest_framework import serializers
from ..models import User,Client,Customer

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','email','is_client']


class CustomerSignupSerializers(serializers.ModelSerializer):
    class Meta:
        password2=serializers.CharField(style={"input_type":"password"},write_only=True)
        model=User
        fields=['username','email','password','password2']
        extra_kwargs={
            'password':{'write_only'}
        }

class ClientSignupSerializers(serializers.ModelSerializer):
    class Meta:
        password2=serializers.CharField(style={"input_type":"password"},write_only=True)
        model=User
        fields=['username','email','password','password2']
        extra_kwargs={
            'password':{'write_only'}
        }