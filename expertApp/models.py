import uuid
from django.db import models
from pagesApp.models import Function
# Create your models here.

class Expert(models.Model):
    expertId = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    firstName = models.CharField(max_length=300, default='')
    email = models.EmailField(max_length=50,default='')
    expertiseFunction = models.ForeignKey(Function,on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return self.firstName