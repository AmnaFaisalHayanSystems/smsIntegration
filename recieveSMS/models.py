from django.db import models

# Create your models here.
from django.contrib.postgres.fields import ArrayField

class SMSstorage(models.Model):
    class Meta:
        verbose_name = "storing received message"
        verbose_name_plural = 'storing received messages'
    created_at = models.DateTimeField(auto_now=True) ## why 'auto_now_add'??
    full_text = models.TextField(blank=True, null=True, )

    phoneNumber = models.IntegerField(default=0)
    
    def __str__(self):
        return "received SMS from " + str(self.phoneNumber)

class sendSMS(models.Model):
    class Meta:
        verbose_name = "storing sent message"
        verbose_name_plural = 'storing sent messages'
    createdAt = models.DateTimeField(auto_now=True) ## why 'auto_now_add'??
    message = models.TextField(blank=True, null=True, )

    phoneNo = models.IntegerField(default=0)
    
    def __str__(self):
        return "SMS sent from " + str(self.phoneNo)        