from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User  
  
class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Blogs(models.Model):
    title = models.CharField(max_length=255)
    picture = models.ImageField(upload_to='blogs/')
    uploaded_on = models.DateTimeField(default=timezone.now)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title
    
class Comments(models.Model):
    blog_post = models.ForeignKey(Blogs, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    content = models.TextField()
    commented_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
