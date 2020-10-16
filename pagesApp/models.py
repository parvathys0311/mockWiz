from django.db import models

# Create your models here.

class Function(models.Model):
    functionID = models.AutoField(primary_key = True)
    functionName = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.functionName


class Role(models.Model):
    roleID = models.AutoField(primary_key = True)
    roleName = models.CharField(max_length=200, default='')
    roleFunction = models.ForeignKey(Function,on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return self.roleName