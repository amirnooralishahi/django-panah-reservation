from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.text import slugify
#jangzade va scan movaqat 

class User(AbstractUser):
    USER_TYPE_CHOICES = [
        ('war_struck', 'War Struck'),
        ('home_owner', 'Home Owner'),
    ]
    user_type = models.CharField(
        max_length=20, 
        choices=USER_TYPE_CHOICES,
        null=True,
        blank=True
    )
class User_war_struck(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    slug=models.SlugField(unique=True)
    email=models.EmailField(null=True)
    phone=PhoneNumberField(blank=True)
    NationalCode = models.CharField(max_length=10, null=True,unique=True)
    Job_title = models.CharField(max_length=100,default='default job')
    picture= models.ImageField(upload_to='profile_picture',null=True,
                               default='default.png')
    def __str__(self):
        return f' {self.user}'
    def save(self,*args, **kwargs): 
        self.slug = str(slugify(self.user)) + str(slugify(self.NationalCode))
        super().save(*args,**kwargs)
    class Meta:
        pass
    


class User_home_owner(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    slug=models.SlugField(unique=True)
    email=models.EmailField(null=True)
    phone=PhoneNumberField(blank=True)
    NationalCode = models.CharField(max_length=10, null=True,unique=True)
    Job_title = models.CharField(max_length=100,default='default job')

    picture= models.ImageField(upload_to='profile_picture',null=True,
                                default='default.png')
    def __str__(self):
        return f' {self.user}'
    def save(self,*args, **kwargs): 
        self.slug = str(slugify(self.user)) + str(slugify(self.NationalCode))
        super().save(*args,**kwargs)
    class Meta:
        pass
    