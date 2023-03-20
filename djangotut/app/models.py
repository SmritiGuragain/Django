from django.db import models

# Create your models here.
class donerModel(models.Model):
    Name= models.CharField(max_length = 100)
    bloodgroupchoices = [
        ('O+ve','O+ve'),
        ('O-ve','O-ve'),
        ('AB+ve','AB+ve'),
    ]
    bloodgroup = models.CharField(choices = bloodgroupchoices, max_length=5)
    Age=models.IntegerField()
    Contact=models.CharField(max_length=15)
    AltContact=models.CharField(max_length=15,blank=True,null=True)
    Address=models.CharField(max_length=200)
    premedhis=models.CharField(max_length=300)
    maritalstatuschoices=[
        ('Single','Single'),
        ('Married','Married',)
    ]
    maritalstatus = models.CharField(choices = maritalstatuschoices, max_length=20,default = 'unmarried')

    def __str__(self):
        return (self.Name + self.bloodgroup)
