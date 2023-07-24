from Admin.models import *
from rest_framework.serializers import ModelSerializer,Serializer,EmailField,CharField,DateField,ChoiceField
from django.core.validators import RegexValidator
from passlib.hash import django_pbkdf2_sha256 as handler


class RecruiterSerilizer(ModelSerializer):
    fname = CharField(
        max_length=255,
        required=False,
        validators=[RegexValidator(r'^[a-zA-Z]*$', 'First name must contain only alphabetical characters.')]
    )
    lname = CharField(
        max_length=255,
        required=False,
        validators=[RegexValidator(r'^[a-zA-Z]*$', 'Last name must contain only alphabetical characters.')]
    )

    contact = CharField(
        max_length=15,
        required=False,
        validators=[RegexValidator(r'^\d*$', 'Contact must contain only numeric characters.')]
    )

    class Meta:
        model = Auth
        fields = ["id",'fname', 'lname', 'email', 'password', 'address', 'contact', 'birthday', 'gender']
        extra_kwargs = {
            'password': {'write_only': True, 'min_length': 8, 'max_length': 16},
        }

    
    def validate(self, data):
        data['password'] = handler.hash(data['password'])
        data['role'] = "recruiter"
        return data
 