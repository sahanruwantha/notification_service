from django.db import models

class Notification(models.Model):
    user_id = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    payload = models.CharField(max_length=200)
    is_read = models.BooleanField(default=False)
