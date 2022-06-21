from smsProject.celery import app
from django.conf import settings
import requests
from recieveSMS.models import sendSMS


@app.task(bind=True)
def send_sms(self, phoneNo, message, id):
    # send_notification(data, subscription_id)
    url = settings.GSM['url_prefix'] + '://' + settings.GSM['phone_ip'] + ":" + settings.GSM['phone_port'] + '/SendSMS?username=' + settings.GSM['app_username'] + '&password=' + settings.GSM['password'] + '&phone=' + str(phoneNo) + '&message=' + message
    res = requests.get(url)
    
    instance = sendSMS.objects.get(id=id)
    instance.error = res.text
    instance.save()
    print(res.text)
    
    return res.text