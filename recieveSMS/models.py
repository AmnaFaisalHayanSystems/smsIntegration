from django.db import models
from django.dispatch import receiver
from django.contrib.postgres.fields import ArrayField
from django.db.models.signals import post_save
from django.conf import settings
import requests

class SMSstorage(models.Model):
    class Meta:
        verbose_name = "storing received message"
        verbose_name_plural = 'storing received messages'
        
    created_at = models.DateTimeField(auto_now_add=True)
    full_text = models.TextField(blank=True, null=True)
    phoneNumber = models.IntegerField(default=0)
    
    def __str__(self):
        return "received SMS from " + str(self.phoneNumber)


class sendSMS(models.Model):
    class Meta:
        verbose_name = "Send message"
        verbose_name_plural = 'Send messages'
        
    createdAt = models.DateTimeField(auto_now_add=True)
    message = models.TextField(blank=True, null=True)
    phoneNo = models.IntegerField(default=0)
    error = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return "SMS sent from " + str(self.phoneNo)     
            
            
@receiver(post_save, sender=sendSMS, dispatch_uid="sendSMSSignal")
def sendSMSSignal(sender, instance, created, **kwargs):
    from recieveSMS.tasks import send_sms
    
    if created:
        send_sms.delay("0" + str(instance.phoneNo), instance.message, instance.id)
            
        