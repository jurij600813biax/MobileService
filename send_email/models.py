from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    post_message = models.CharField(max_length=20)
    text_message = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

class Settings_common(models.Model):
    """видимость другим"""
    VIS = 'Yes'
    INVIS = 'No'

    DETAIL_VISIBILITY = ((VIS, 'Yes'), (INVIS, 'No'))

    number_reg_letter = models.CharField(max_length=5, default='NUM')
    number_reg_start = models.IntegerField(default=0)
    message_send_start = models.CharField(max_length=5, default='9.00')
    message_send_finish = models.CharField(max_length=5, default='17.00')
    details_visible = models.CharField(max_length=10, choices=DETAIL_VISIBILITY)
    type_message = models.CharField(max_length=20)
    contact_number = models.CharField(max_length=20)
    free_set = models.CharField(max_length=20, choices=DETAIL_VISIBILITY)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

class Send_message(models.Model):
    send_message_start = models.CharField(max_length=5)
    send_message_finish = models.CharField(max_length=5)
    send_message_text = models.TextField()
    send_message_email = models.EmailField(max_length=254)
    send_message_number_tel = models.CharField(max_length=20)
    send_message_sticker = models.CharField(max_length=5)
    send_message_price = models.CharField(max_length=5)
    send_message_date = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)