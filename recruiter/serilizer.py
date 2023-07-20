from rest_framework import serializers
import Usable.usable as uc
from Admin.models import *
from passlib.hash import django_pbkdf2_sha256 as handler

class serRegistration(serializers.ModelSerializer):
    class Meta:
        model = Auth
        fields = '__all__'

    

    def validate(self, data):
        ##reqyuired keys and data not empty validation
        validator = uc.keyValidation(True,True,self.context['request'].data,self.context['requireFields'])
        if validator:
            raise serializers.ValidationError({"error":validator["message"]})
        
        ##email validation
        if not uc.checkemailforamt(data['email']):
            raise serializers.ValidationError({"error":"email is not valid"})
        
        #password length validation
        if not uc.passwordLengthValidator(data['password']):
            raise serializers.ValidationError({"error":"password must be 8 or less than 20 characters"})

        

        #number not allowed Validation
        if uc.has_numbers(data['fname']) or uc.has_numbers(data['lname']):
            raise serializers.ValidationError({"error":"fname,lname should not be include any number"})


        #characters not allowed in a Contact number
        if not uc.has_numbers(data['contact'],True):
            raise serializers.ValidationError({"error":"Contact number should not be include any characters"})


        ##Check already exists Validation
        checkalready = Auth.objects.filter(email = data['email']).first()
        if checkalready:
            raise serializers.ValidationError({"error":"Email already exists"})


        data['password'] = handler.hash(data['password'])
        data['role'] = self.context['role']
        return data



class serGetrecruiter(serializers.ModelSerializer):
    class Meta:
        model = Auth
        fields = ['id','fname','lname','email','address','contact','status','profile','birthday','gender']



