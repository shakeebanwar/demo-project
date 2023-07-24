from rest_framework.permissions import BasePermission
from rest_framework.exceptions import APIException
from rest_framework import status
from decouple import config
import jwt
from Admin.models import WhitelistToken

##Only for admin
class Authorization(BasePermission):

    def has_permission(self, request, view):
        try:
            tokencatch = request.META['HTTP_AUTHORIZATION'][7:]
            request.GET._mutable = True
            my_token = jwt.decode(tokencatch,config('superadminjwttoken'), algorithms=["HS256"])
            request.GET['token'] = my_token
            WhitelistToken.objects.get(user = my_token['id'],token = tokencatch)
            return True
            
        except:
            raise NeedLogin()

#Only for recruiter
class RecruiterPermission(BasePermission):

    def has_permission(self, request, view):
        try:
            tokencatch = request.META['HTTP_AUTHORIZATION'][7:]
            request.GET._mutable = True
            my_token = jwt.decode(tokencatch,config('recruiter'), algorithms=["HS256"])
            request.GET['token'] = my_token
            WhitelistToken.objects.get(user = my_token['id'],token = tokencatch)
            return True
        
        except:
            raise NeedLogin()

##Combine 
class CombineAuthorization(BasePermission):

    def has_permission(self, request, view):
        try:
            role = request.GET['role']
            tokencatch = request.META['HTTP_AUTHORIZATION'][7:]
            request.GET._mutable = True

            if role == "superadmin":
                my_token = jwt.decode(tokencatch,config('superadminjwttoken'), algorithms=["HS256"])
                request.GET['token'] = my_token
                WhitelistToken.objects.get(user = my_token['id'],token = tokencatch)
                return True

            
            elif role == "recruiter":
                my_token = jwt.decode(tokencatch,config('recruiter'), algorithms=["HS256"])
                request.GET['token'] = my_token
                WhitelistToken.objects.get(user = my_token['id'],token = tokencatch)
                return True

            else:
                raise NeedLogin()

        except:
            raise NeedLogin()


class NeedLogin(APIException):
    status_code = 422
    default_detail = {'status': False, 'message': 'Unauthorized'}
    default_code = 'not_authenticated'