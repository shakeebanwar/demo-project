from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import Usable.usable as uc
from Usable.permission import *
from .serilizer import *
from django.conf import settings
from Usable.permission import *
from django.db.models import F

# Create your views here.
class registration(APIView):
    permission_classes = [authorization]

    def get_permissions(self, *args, **kwargs):
        if self.request.method in ['GET']:
            return [authorization()]
        else:
            return []


    def get(self,request):
        try:
            data = Auth.objects.filter(role = "recruiter").order_by('-created_at')
            serdata = serGetrecruiter(data,many = True).data
            return Response({"status":True,"data":serdata})

        except Exception as e:
            message = {'status':False}
            message.update(message=str(e))if settings.DEBUG else message.update(message='Internal server error')
            return Response(message,status=500)



    def post(self,request):
        try:
            requireFields = ['fname','lname','email','password','address','contact','birthday','gender']
            val = serRegistration(data = request.data,context = {'request':request,"requireFields":requireFields,"role":"recruiter"})
            
            if val.is_valid():
                val.save()

                #choose specific keys
                finaldata = uc.removeDic(val.data,['updated_at','created_at','password','status','contact','birthday','profile','Otp','OtpCount','category'])
                return Response({"status":True,"message":"Account Created Successfully","data":finaldata},status = 201)

            else:
                error = uc.execptionhandler(val)
                return Response({'status':False,'message':error},status=422)

        except Exception as e:
            
            message = {'status':False}
            message.update(message=str(e))if settings.DEBUG else message.update(message='Internal server error')
            return Response(message,status=500)



