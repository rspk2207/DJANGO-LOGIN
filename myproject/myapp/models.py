from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
class student(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=50,default='')
    roll_number = models.CharField(max_length = 50,default='')
    college = models.CharField(max_length=50,default='')
    year = models.CharField(max_length=10,default='')
    gender = models.CharField(max_length=5,default='')

@receiver(post_save, sender = User)
def create_user(sender,instance,created,**kwargs):
    if created:
        student.objects.create(user = instance)

@receiver(post_save,sender = User)
def save_user(sender,instance,**kwargs):
    instance.student.save()