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
    email = models.CharField(max_length=255, blank=False,null=False)
    password=models.TextField(blank=False,null=False)
    address = models.TextField(blank=True,null=True)
    contact = models.CharField(max_length=15,blank=True,null=True)
    status=models.BooleanField(default=False)
    role = models.CharField(choices = user_role,max_length=10,default="applicant",blank=False,null=False)
    profile= models.ImageField(upload_to='Auth/',default="Auth/dummy.jpg")
    Otp = models.IntegerField(default=0)
    OtpStatus = models.BooleanField(default=False)
    OtpCount = models.IntegerField(default=0)
    birthday =  models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=10, null=True,blank=True,choices = Gender)
    
    def __str__(self):
        return self.fname


class whitelistToken(models.Model):
    user = models.ForeignKey(Auth, on_delete =models.CASCADE)
    token = models.TextField(default="")
    created_at = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    useragent = models.TextField(default="")




