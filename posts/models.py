from django.db import models
from django.contrib.auth.models import User
from users.models import Profile


# Create your models here.

class Post(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile,  on_delete=models.CASCADE)
    title = models.CharField( max_length=200)
    photo = models.ImageField( upload_to='posts/photos')
    created = models.DateTimeField( auto_now=False, auto_now_add=True)
    modified = models.DateTimeField( auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.title
    