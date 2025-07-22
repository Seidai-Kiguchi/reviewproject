from django.db import models
from django.contrib.auth.models import User

# Create your models here.
EVALUATION_CHOICES = [('良い','良い'),('悪い','悪い')]
class ReviewModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    images = models.ImageField(upload_to='images/', blank=True, null=True)
    useful_review = models.IntegerField(null=True, blank=True, default=0)
    useful_review_record = models.TextField(blank=True,default="")
    evaluation = models.CharField(max_length=10, choices = EVALUATION_CHOICES)

    def __str__(self):
        return self.title