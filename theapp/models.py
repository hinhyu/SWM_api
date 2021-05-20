from django.db import models

# Create your models here.
class userInfo(models.Model):
    name = models.CharField(max_length=10)
    age = models.IntegerField()
    address = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:ordering = ['created']