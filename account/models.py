from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
import os
from PIL import Image
class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    secret_key = models.CharField(blank=True, null=True, max_length=100)
    otp_created_at = models.DateTimeField(blank=True, null=True)
    is_email_verified = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return f" {self.username}"



class Profile(models.Model):
    id=models.UUIDField(editable=False,primary_key=True,unique=True,default=uuid.uuid4)
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    image=models.ImageField(upload_to="profiles/", default="default/avatar.jpg")
    bio=models.TextField(max_length=500)
    date_joined=models.DateTimeField(auto_now_add=True)
    last_updated=models.DateTimeField(auto_now=True)
     
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.image and os.path.isfile(self.image.path):
            img = Image.open(self.image.path)
            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                img.save(self.image.path)

    def __str__(self):
        return f'{self.user.username} Profile'