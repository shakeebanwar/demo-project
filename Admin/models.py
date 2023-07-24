from django.db import models
import uuid

# Create your models here.
user_role =(
    ("superadmin", "superadmin"),
    ("recruiter", "recruiter"),
    ("applicant", "applicant"),
    
)

Gender = (
    ("male", "male"),
    ("female", "female"),
    ("others", "others"),
    
)


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    updated_at = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True,blank=True, null=True)

    class Meta:
        abstract = True

class Auth(BaseModel):

    fname = models.CharField(max_length=255, blank=True,null=True)
    lname = models.CharField(max_length=255, blank=True,null=True)
    email = models.EmailField(blank=False,null=False,unique = True)
    password=models.TextField(blank=False,null=False,max_length=255)
    address = models.TextField(blank=True,null=True)
    contact = models.CharField(max_length=15,blank=True,null=True)
    status=models.BooleanField(default=False)
    role = models.CharField(choices = user_role,max_length=10,default="applicant",blank=False,null=False)
    profile= models.ImageField(upload_to='Auth/',default="Auth/dummy.jpg")
    Otp = models.PositiveSmallIntegerField(default=0)
    OtpStatus = models.BooleanField(default=False)
    OtpCount = models.IntegerField(default=0)
    birthday =  models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=10, null=False,blank=False,choices = Gender)
    
    def __str__(self):
        return f"{self.fname} {self.lname} - {self.email}"



class WhitelistToken(models.Model):
    user = models.ForeignKey(Auth, on_delete =models.CASCADE)
    token = models.TextField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    useragent = models.TextField(blank=False, null=False)




