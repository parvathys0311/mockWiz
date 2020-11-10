
# Create your models here
import uuid

from django.db import models

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
    expertId = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    firstName = models.CharField(max_length=300, default='')
    lastname = models.CharField(max_length=300, default='')
    email = models.EmailField(max_length=50,default='')
    expertiseFunction = models.ForeignKey(Function,on_delete=models.CASCADE,default='')
    linkedInUrl = models.URLField(max_length=400, default='')
    yearsInterviewedFor = models.CharField(max_length=12, choices=YEAR_CHOICES,default='')
    approved = models.CharField(max_length=1, choices=YN_CHOICES,default='N', null=True, blank=True)

    def __str__(self):
        return self.firstName
