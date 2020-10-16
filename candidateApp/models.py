import uuid

from django.db import models

# Create your models here.
from pagesApp.models import Role


class Candidate(models.Model):
    candidateId = models.UUIDField(primary_key=True,default=uuid.uuid4().hex[:6].upper(), editable=False)
    firstName = models.CharField(max_length=300, default='')
    email = models.EmailField(max_length=50,default='')
    interestedRole = models.ForeignKey(Role,on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return self.firstName