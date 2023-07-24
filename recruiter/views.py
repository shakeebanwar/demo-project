from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from Usable.usable import UsableComponent
from Usable.permission import *
from .serializer import *
from django.conf import settings
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from Admin.serializer import ProfileSerializer
from Usable.usable import CustomPageNumberPagination

# Create your views here.

class Registration(ModelViewSet):
    @action(detail=False, methods=['post'])
    def signup(self,request):
        try:
            serializer = RecruiterSerilizer(data=request.data)
            if not serializer.is_valid():
                error = UsableComponent.execptionhandler(serializer)
                return Response({"status": False, "message": error}, status=422)
            
            serializer.save()
            return Response({"status": True, "message":"Account Created Successfully","data":serializer.data},status=201)

        
        except Exception as e:
            return Response({'status':False,'errors':str(e)},status=403)

    @action(detail=False, methods=['get'],permission_classes = [Authorization])
    def allrecruiter(self,request):
        try:
            data = Auth.objects.filter(role="recruiter").order_by('-created_at')
            paginator = CustomPageNumberPagination()
            paginated_data = paginator.paginate_queryset(data, request)
            serdata = ProfileSerializer(paginated_data, many=True).data
            return paginator.get_paginated_response({"status": True, "data": serdata})

        except Exception as e:
            return Response({'status':False,'errors':str(e)},status=403)

