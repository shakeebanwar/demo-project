from .models import *
from rest_framework.serializers import ModelSerializer,Serializer,EmailField,CharField

#for login
class LoginSerializer(Serializer):
    email = EmailField(required=True)
    password = CharField(required=True, write_only=True,min_length=8, max_length=16)


#for change password
class ChangePasswordSerializer(Serializer):
    oldpassword = CharField(required=True, write_only=True,min_length=8, max_length=16)
    password = CharField(required=True, write_only=True,min_length=8, max_length=16)

#show profile

class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Auth
        fields = ["id","fname","lname","email","profile","address","contact"]
