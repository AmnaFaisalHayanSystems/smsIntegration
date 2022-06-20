from recieveSMS.models import SMSstorage
import requests

def storeMessage(_phoneNumber , _message):
    try:
        SMSstorage.objects.create(
            text = _message,
            phoneNumber = _phoneNumber
            )
        print("received SMS stored")
    except:
        print("received SMS not stored.")
        return False
    finally:
        return True

def setUrl(phone,message):
   url = 'http://192.168.1.2:8090/SendSMS?username=waheed&password=waheed&phone='+phone+'&message='+message
   x = requests.get(url)
   print(x.text)
   return(x.text)