from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from passlib.hash import django_pbkdf2_sha256 as handler
from .serializer import *
import Usable.usable as uc
from decouple import config
from Usable.permission import *
from django.conf import settings
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action

# Create your views here.
class Authentication(ModelViewSet):
    @action(detail=False, methods=['post'])
    def login(self,request):
        try:
            serializer = LoginSerializer(data=request.data)
            if not serializer.is_valid():
                error = uc.execptionhandler(serializer)
                return Response({'status': False, 'message': error}, status=422)

            email = serializer.validated_data['email']
            password = serializer.validated_data['password']

            fetchuser = Auth.objects.filter(email=email).first()
            if not fetchuser or not handler.verify(password, fetchuser.password):
                return Response({'status': False, 'message': 'Invalid Credential'}, status=403)

            if not fetchuser.status:
                return Response({'status': False, 'message': 'Your Account is not active'}, status=403)

            jwtkeys = {
                "superadmin": config("superadminjwttoken"),
                "recruiter": config("recruiter"),
                "applicant": config("applicant")
            }

            jwt_token = jwtkeys.get(fetchuser.role)
            generate_auth = uc.generatedToken(fetchuser, jwt_token, 1, request)

            if not generate_auth['status']:
                return Response(generate_auth, status=500)

            return Response({
                'status': True,
                'message': 'Login Successfully',
                'token': generate_auth['token'],
                'data': generate_auth['payload']
            }, status=200)


        except Exception as e:
            return Response({'status':False,'errors':str(e)},status=403)
        
    
    @action(detail=False, methods=['post'],permission_classes = [Authorization])
    def logout(self,request):
        try:
            token_id = request.GET['token']['id']
            authorization_header = request.META.get('HTTP_AUTHORIZATION')
            token = authorization_header[7:]

            if uc.blacklisttoken(token_id, token):
                return Response({'status': True, 'message': 'Logout successfully'}, status=200)
            else:
                return Response({'status': False, 'message': 'Incorrect userid'}, status=403)
        
        except Exception as e:
            return Response({'status':False,'errors':str(e)},status=403)


    
    @action(detail=False, methods=['post'],permission_classes = [Authorization])
    def changepassword(self,request):
        try:
            serializer = ChangePasswordSerializer(data=request.data)
            if not serializer.is_valid():
                error = uc.execptionhandler(serializer)
                return Response({'status': False, 'message': error}, status=422)
            
            old_password = serializer.validated_data['oldpassword']
            new_password = serializer.validated_data['password']
            token = request.META['HTTP_AUTHORIZATION'][7:]
            user_id = request.GET['token']['id']
            user = Auth.objects.filter(id = user_id).first()

            if not handler.verify(old_password, user.password):
                return Response({'status': False, 'message': 'Your Old Password is Wrong'}, status=403)

            if handler.verify(new_password, user.password):
                return Response({'status': False, 'message': 'You choose old password, try another one'}, status=403)
            

            user.password = handler.hash(new_password)
            user.save()
            uc.blacklisttoken(user_id,token)
            return Response({'status':True,'message':'Password Update Successfully'})


        except Exception as e:
            return Response({'status':False,'errors':str(e)},status=403)



class AdminProfile(ModelViewSet):
    @action(detail=False, methods=['get'],permission_classes = [Authorization])
    def viewprofile(self, request):
        try:
            userid = request.GET['token']['id']
            fetchuser = Auth.objects.filter(id = userid).first()
            serUser = ProfileSerializer(fetchuser).data
            return Response({"status":True,"data":serUser})
        
        except Exception as e:
            return Response({'status':False,'errors':str(e)},status=403)



class AccountActivation(ModelViewSet):
    @action(detail=False, methods=['post'],permission_classes = [Authorization])

    def activedisable(self, request):
        try:
            message = {True:"Account Activation successfully",False:"Account Deactivate successfully"}
            id = request.data['id']
            fetchdata = Auth.objects.filter(id = id).first()
            fetchdata.status = not fetchdata.status
            fetchdata.save()
            return Response({"status":fetchdata.status,"message":message[fetchdata.status]})

        except Exception as e:
            return Response({'status':False,'errors':str(e)},status=403)

