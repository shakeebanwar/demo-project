from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from passlib.hash import django_pbkdf2_sha256 as handler
from .serilizer import *
import Usable.usable as uc
from decouple import config
from Usable.permission import *
from django.conf import settings
from operator import itemgetter
import random
from django.db.models import F
# Create your views here.


class login(APIView):
    def post(self,request):
        try:
            requireFields = ["email","password"]
            val = serLogin(data = request.data,context = {'request':request,"requireFields":requireFields})
            if val.is_valid():
                email = request.data['email']
                password = request.data['password']
                fetchuser = Auth.objects.filter(email = email).first()
                if fetchuser and handler.verify(password,fetchuser.password):
                    if fetchuser.status:
                        jwtkeys = {"superadmin":config("superadminjwttoken"),"recruiter":config("recruiter"),"applicant":config("applicant")} 
                        generate_auth = uc.generatedToken(fetchuser,jwtkeys[fetchuser.role],1,request)
                        
                        if generate_auth['status']:
                            return Response({'status':True,'message':'Login SuccessFully','token':generate_auth['token'],'data':generate_auth['payload']},status=200)

                        else:
                            return Response(generate_auth)
                    
                    
                    else:
                        return Response({'status':False,'message':'Your Account is not active'})



                else:
                    return Response({'status':False,'message':'Invalid Credential'},status=403)




            else:
                error = uc.execptionhandler(val)
                return Response({'status':False,'message':error},status=422)



        except Exception as e:
            message = {'status':False}
            message.update(message=str(e))if settings.DEBUG else message.update(message='Internal server error')
            return Response(message,status=500)





class logout(APIView):
    permission_classes = [combineAuthorization]

    def get(self,request):
        try:
            res = {True:{"status":True,"message":"logout successfully"},False:{"status":False,"message":"Something went wrong"}}
            
            fetch = uc.blacklisttoken(request.GET['token']['id'],request.META['HTTP_AUTHORIZATION'][7:])
            return Response(res[fetch])



        except Exception as e:
            message = {'status':False}
            message.update(message=str(e))if settings.DEBUG else message.update(message='Internal server error')
            return Response(message,status=500)






class changepassword(APIView):
    permission_classes = [combineAuthorization]

    def post(self,request):
        try:
            requireFields = ['oldpassword','password']
            validator = uc.keyValidation(True,True,request.data,requireFields)
            if validator:
                return Response(validator,status = 403)

            else:
                data = Auth.objects.filter(id = request.GET['token']['id']).first()
                if handler.verify(request.data['oldpassword'],data.password):
                    ##check if user again use old password
                    if not handler.verify(request.data['password'],data.password):
                        
                        #password length validation
                        passwordStatus = uc.passwordLengthValidator(request.data['password'])
                        if not passwordStatus:
                            return Response({"status":False,"message":"Password must be 8 or less than 20 characters"})
                    
                        data.password = handler.hash(request.data['password'])
                        data.save()

                        ## black list token
                        uc.blacklisttoken(request.GET['token']['id'],request.META['HTTP_AUTHORIZATION'][7:])
                        return Response({'status':True,'message':'Password Update Successfully'})

                    else:
                        return Response({'status':False,'message':'You choose old password try another one'})


                else:
                    return Response({'status':False,'message':'Your Old Password is Wrong'})

        

        except Exception as e:
            message = {'status':False}
            message.update(message=str(e))if settings.DEBUG else message.update(message='Internal server error')
            return Response(message,status=500)





class profile(APIView):
    permission_classes = [combineAuthorization]

    def get(self,request):
        try:
            fetchuser = Auth.objects.filter(id = request.GET['token']['id']).first()
            access_token_payload = {
                "id":fetchuser.id,
                "fname":fetchuser.fname,
                "lname":fetchuser.lname,
                "email":fetchuser.email,
                "profile":fetchuser.profile.url,
                "address":fetchuser.address,
                "contact":fetchuser.contact
            }

            return Response({"status":True,"data":access_token_payload})


        except Exception as e:
            message = {'status':False}
            message.update(message=str(e))if settings.DEBUG else message.update(message='Internal server error')
            return Response(message,status=500)



    
    
    def put(self,request):
        try:
            requireFields = ['fname','lname','address','contact']
            validator = uc.keyValidation(True,True,request.data,requireFields)
            if validator:
                return Response(validator,status = 200)

            else:
                fetchuser = Auth.objects.filter(id = request.GET['token']['id']).first()
                fetchuser.fname, fetchuser.lname,fetchuser.address, fetchuser.contact = itemgetter('fname', 'lname','address','contact')(request.data)

                if request.data.get('img',False):
                    fetchuser.profile = request.data['img']

                fetchuser.save()
                obj = uc.makedict(fetchuser,['id','fname','lname','address','contact','email','profile'],True)
                return Response({"status":True,"message":"Update Successfully","data":obj})



        except Exception as e:
            message = {'status':False}
            message.update(message=str(e))if settings.DEBUG else message.update(message='Internal server error')
            return Response(message,status=500)



class accountActivation(APIView):
    permission_classes = [authorization]

    def get(self, request):
        try:
            message = {True:"Account Activation successfully",False:"Account Deactivate successfully"}
            id = request.GET['id']
            fetchdata = Auth.objects.filter(id = id).first()
            fetchdata.status = not fetchdata.status
            fetchdata.save()
            return Response({"status":fetchdata.status,"message":message[fetchdata.status]})

        except Exception as e:
            message = {'status':False}
            message.update(message=str(e))if settings.DEBUG else message.update(message='Internal server error')
            return Response(message,status=500)




class alljobs(APIView):
    permission_classes = [authorization]

    def get(self,request):
        try:
            fetchdata = jobsapplication.objects.all().order_by('-created_at').values("id","title","location","worktime","jobrole","jobrequirements","status",created = F("created_at__date"),updated = F('updated_at__date'),firstname = F("jobwriter__fname"),lastname = F('jobwriter__lname'),jobtype = F("category__name"))
            return Response({"status":True,"data":fetchdata})

        
        
        except Exception as e:
            message = {'status':False}
            message.update(message=str(e))if settings.DEBUG else message.update(message='Internal server error')
            return Response(message,status=500)



