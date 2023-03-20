from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class info(models.Model):
    Name=models.CharField(max_length=20)
    Description=RichTextField(blank=True,null=True)
    Photo=models.ImageField(upload_to='images',default='NULL',blank=True,null=True)
    Created=models.DateTimeField(auto_now_add=True)
    Categorychoices=[
        ('Certificate','Certificate'),
        ('Cat','Cat')
    ]
    Category=models.CharField(choices=Categorychoices,max_length=20)
    def  __str__(self):
        return self.Name