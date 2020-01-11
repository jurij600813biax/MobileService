from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    post_message = models.CharField(max_length=20)
    text_message = models.TextField()
    type_message = models.CharField(max_length=20)
    reg_num_set = models.CharField(max_length=20)
    free_set = models.CharField(max_length=20)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)