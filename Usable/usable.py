from datetime import datetime,timedelta
from django.utils import timezone
import jwt
from Admin.models import WhitelistToken
from rest_framework.pagination import PageNumberPagination
from django.core.exceptions import ObjectDoesNotExist


##generate jwt token and return userinfo
def generatedToken(fetchuser,authKey,totaldays,request):
    try:
        access_token_payload = {
            'id': str(fetchuser.id),
            'iat': timezone.now(),
            'exp': timezone.now() + timedelta(days=totaldays)

        }
        userpayload = { 'id': str(fetchuser.id),'email':fetchuser.email,'fname':fetchuser.fname,'lname':fetchuser.lname,'profile':fetchuser.profile.url,'role':fetchuser.role}
        access_token = jwt.encode(access_token_payload,authKey, algorithm='HS256')
        
        WhitelistToken(user = fetchuser,token = access_token,useragent = {"useragent":request.META['HTTP_USER_AGENT'],"ip":request.META.get('HTTP_X_FORWARDED_FOR')}).save()
        return {"status":True,"token":access_token,"payload":userpayload}

    except Exception as e:
        return {"status":False,"message":"Something went wrong in token creation","details":str(e)}



## blacklist jwt token
def blacklisttoken(id, token):
    try:
        WhitelistToken.objects.get(user=id, token=token).delete()
        return True
    except ObjectDoesNotExist:
        return False



def execptionhandler(val):
    if 'error' in val.errors:
        error = val.errors["error"][0]
    else:
        key = next(iter(val.errors))
        error = key + ", "+val.errors[key][0]

    return error


class CustomPageNumberPagination(PageNumberPagination):
    page_size = 10  
