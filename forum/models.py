from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now




class Profile(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)    
    
    
    
class Post(models.Model):
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    post_id = models.AutoField
    post_content = models.CharField(max_length=5000)
    timestamp = models.DateTimeField(default=now)
    likes = models.DecimalField(max_digits=5, decimal_places=0)



