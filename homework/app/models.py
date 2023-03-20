from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class homework(models.Model):
    Titlechoices=[
        ('LAB','LAB'),
        ('Assignment','Assignment'),
        ('Note','Note'),
        ('Notice','Notice'),
    ]
    Title=models.CharField(choices=Titlechoices,max_length=15)
    Semesterchoices=[
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
        ('6','6'),
        ('7','7'),
        ('8','8'),
    ]
    Semester=models.CharField(choices=Semesterchoices,max_length=2)
    Description=RichTextField(blank=True,null=True)
    work=models.FileField()

    def __str__(self):
        return self.Title
    