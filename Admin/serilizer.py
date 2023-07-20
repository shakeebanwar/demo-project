from .models import *
from rest_framework import serializers
import Usable.usable as uc



class serLogin(serializers.ModelSerializer):
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

        return data






