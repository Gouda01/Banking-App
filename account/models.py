from django.db import models
import uuid
from shortuuid.django_fields import ShortUUIDField
from django.db.models.signals import post_save

from userauths.models import User


# Create your models here.


ACCOUNT_STATUS = {
    ("active", "Active"),
    ("in-active", "In-active"),
}

MARITAL_STATUS = {
    ("married", "Married"),
    ("single", "Single"),
    ("other", "Other"),
}

GENDER = {
    ("male", "Male"),
    ("female", "Female"),
}

IDENTY_TYPE = {
    ("national_id_card", "National ID Card"),
    ("drivers_licence", "Drivers Licence"),
    ("international_passport", "International Passport"),
}



def user_directory_path(instance, filename):
    ext = filename.split(".")[-1]
    filename = "%s_%s" % (instance.id, ext)
    return "user_{0}/{1}".format(instance.user.id, filename)

class Account(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    account_balance = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    account_number = ShortUUIDField(unique=True, length=10, max_length=25, prefix="217", alphabet="1234567890")
    account_id = ShortUUIDField(unique=True, length=7, max_length=25, prefix="Dex", alphabet="1234567890")
    pin_number = ShortUUIDField(unique=True, length=4, max_length=7, alphabet="1234567890")
    red_code = ShortUUIDField(unique=True, length=10, max_length=20, alphabet="abcdefgh1234567890")
    account_status = models.CharField(max_length=50, choices=ACCOUNT_STATUS, default="in-active")
    date = models.DateTimeField(auto_now_add=True)
    kyc_submitted = models.BooleanField(default=False)
    kyc_confirmed = models.BooleanField(default=False)
    recommended_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='recommended_by')

    class Meta :
        ordering = ['-date']

    def __str__(self):
        try:
            return str(self.user)
        except:
            return "Account Model"
        

def create_account (sender, instance, created, **kwargs):
    if created:
        Account.objects.create(user=instance)

def save_account(sender, instance, **kwargs):
    instance.account.save()

post_save.connect(create_account, sender=User)
post_save.connect(save_account, sender=User)

    

class KYC(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    full_name = models.CharField(max_length=1000)
    image = models.ImageField(upload_to="kyc", default="kyc/default.jpg")
    marrital_status = models.CharField(choices=MARITAL_STATUS, max_length=40)
    gender = models.CharField(choices=GENDER, max_length=40)
    identity_type = models.CharField(choices=IDENTY_TYPE, max_length=140)
    identity_image = models.ImageField(upload_to="kyc", null=True, blank=True)
    date_of_birth = models.DateField(auto_now_add=False)
    signature = models.ImageField(upload_to="kyc")

    #Address :
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    #Contact Details :
    mobile = models.CharField(max_length=100)
    fax = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)
    