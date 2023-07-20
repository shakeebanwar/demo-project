from decouple import config
import re
from PIL import Image
import datetime
import jwt
from Admin.models import whitelistToken



def requireKeys(reqArray,requestData):
    """Check if all required keys are present in the request data."""
    return all(key in requestData for key in reqArray)




def allfieldsRequired(reqArray,requestData):
    """Check if all required fields have values in the request data."""
    return all(requestData.get(key) for key in reqArray)

            



def checkemailforamt(email):
    emailregix = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    if(re.match(emailregix, email)):
        return True

    else:
        return False



def imageValidator(img,ignoredimension = True,formatcheck = False):

    try:

        if img.name[-3:] == "svg":
            return True

        im = Image.open(img)
        width, height = im.size
        if ignoredimension:
            if width > 330 and height > 330:
                return False

            else:
                return True

        if formatcheck:
            if im.format == "PNG":
                
                return True

            else:
                
                return False

        return True
            

    
    except:
        return False
        




def passwordLengthValidator(passwd):
    if len(passwd) >= 8 and len(passwd) <= 20:
        return True

    else:
        return False



##both keys and required field validation

def keyValidation(keyStatus,reqStatus,requestData,requireFields):


    ##keys validation
    if keyStatus:
        keysStataus = requireKeys(requireFields,requestData)
        if not keysStataus:
            return {'status':False,'message':f'{requireFields} all keys are required'}



    ##Required field validation
    if reqStatus:
        requiredStatus = allfieldsRequired(requireFields,requestData)
        if not requiredStatus:
            return {'status':False,'message':'All Fields are Required'}




def key_validation(key_status, req_status, request_data, require_fields):
    """Validate keys and required fields in the request data."""
    if key_status and not require_keys(require_fields, request_data):
        return {'status': False, 'message': f'{require_fields} all keys are required'}

    if req_status and not all_fields_required(require_fields, request_data):
        return {'status': False, 'message': 'All Fields are Required'}

    return {'status': True}












def generatedToken(fetchuser,authKey,totaldays,request):
    try:
        access_token_payload = {
            'id': str(fetchuser.id),
            'email':fetchuser.email,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=totaldays),
            'iat': datetime.datetime.utcnow(),

        }
        
        userpayload = { 'id': str(fetchuser.id),'email':fetchuser.email,'fname':fetchuser.fname,'lname':fetchuser.lname,'profile':fetchuser.profile.url,'role':fetchuser.role}
    
        access_token = jwt.encode(access_token_payload,authKey, algorithm='HS256')

        whitelistToken(user = fetchuser,token = access_token,useragent = {"useragent":request.META['HTTP_USER_AGENT'],"ip":request.META.get('HTTP_X_FORWARDED_FOR')}).save()

        return {"status":True,"token":access_token,"payload":userpayload}

    except Exception as e:
        return {"status":False,"message":"Something went wrong in token creation","details":str(e)}






def blacklisttoken(id,token):
    try:
        whitelistToken.objects.get(user = id,token = token).delete()
        return True
    
    except:
        return False


#check no,characters validation
def has_numbers(inputString,charcters = False):
    if charcters:
        return all(char.isdigit() for char in inputString)

    else:
        return any(char.isdigit() for char in inputString)






def makedict(obj,key,imgkey=False):
    dictobj = {}
    for j in range(len(key)):
        dictobj[key[j]] = getattr(obj,key[j])
    
    if imgkey:
        dictobj[key[-1]] = getattr(obj,key[-1]).url

    return dictobj




##Date Validation
def dateValidate(date_text):
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
        return True
            
    except ValueError:
        return False



##Remove multiple keys in a dictionay

def removeDic(dictdata,checkarray):
    for key in checkarray:
        if key in dictdata:
            del dictdata[key]
    

    return dictdata


#serilizers valdation error exceptions

def errorHandler(val,msg):
    try:
        return val["error"][0]

    except:
        return msg


def execptionhandler(val):
    if 'error' in val.errors:
        error = val.errors["error"][0]
    else:
        key = next(iter(val.errors))
        error = key + ", "+val.errors[key][0]

    return error



































































































