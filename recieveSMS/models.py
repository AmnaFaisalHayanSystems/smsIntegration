from django.db import models

# Create your models here.
from django.contrib.postgres.fields import ArrayField

class SMSstorage(models.Model):
    class Meta:
        verbose_name = "storing recieved message"
        verbose_name_plural = 'storing recived messages'
    created_at = models.DateTimeField(auto_now=True) ## why 'auto_now_add'??
    full_text = models.TextField(blank=True, null=True, )

    phoneNumber = models.IntegerField(default=0)
    
    def __str__(self):
        return "recieved SMS from " + str(self.phoneNumber)