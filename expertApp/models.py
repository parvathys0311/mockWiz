from django.db.models.signals import pre_save
from phone_field import PhoneField
# Create your models here
import uuid

from django.db import models

from mockWizProject.utils import unique_slug_generator
from pagesApp.models import Function

YEAR_CHOICES = (
    ('','Years of interviewing experience'),
    ('lessThanOne','Less than 1 year'),
    ('oneToThree', '1 - 3 years'),
    ('threeToFive', '3 - 5 years'),
    ('fiveToTen', '5 - 10 years'),
    ('moreThanTen', 'More than 10 years')
)

YN_CHOICES = (
    ('Y','Yes'),
    ('N','No'),
)

class Expert(models.Model):
    # expertId = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    expertId = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=300, default='')
    lastname = models.CharField(max_length=300, default='')
    email = models.EmailField(max_length=50,default='')
    expertiseFunction = models.ForeignKey(Function,on_delete=models.CASCADE,default='')
    linkedInUrl = models.URLField(max_length=400, default='')
    yearsInterviewedFor = models.CharField(max_length=12, choices=YEAR_CHOICES,default='')
    approved = models.CharField(max_length=1, choices=YN_CHOICES,default='N', null=True, blank=True)

    phoneNumber = PhoneField(help_text='Contact phone number',default='',blank=True)
    jobTitle = models.CharField(max_length=100, default='', blank=True)
    organization = models.CharField(max_length=200, default='', blank=True)
    imageProfile = models.ImageField(upload_to='expert/profilePicture', default='./mockWizProject/static/images/default.png', blank=True)
    city = models.CharField(max_length=100, default='', blank=True)
    country = models.CharField(max_length=100, default='', blank=True)
    summary = models.TextField(default='')
    slug = models.SlugField(max_length=250,null=True,blank=True)

    def __str__(self):
        return self.firstName

def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(slug_generator, sender=Expert)