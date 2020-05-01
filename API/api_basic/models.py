from django.db import models

# Create your models here.

class Articles(models.Model):
    Topic= models.CharField(max_length=100)
    memoryverse = models.TextField()
    writing = models.TextField()
    month = models.CharField(max_length=100)
    Date = models.CharField(max_length=100)

    def __str__(self):
        return self.Topic

class Register(models.Model):
    username= models.CharField(max_length=100)
    gmail = models.CharField(max_length=100)
    Date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
