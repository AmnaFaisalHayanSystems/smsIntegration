from recieveSMS.models import SMSstorage
from recieveSMS.models import sendSMS
import requests

def storeMessage(_phoneNumber , _message):
    try:
        SMSstorage.objects.create(
            full_text = _message,
            phoneNumber = _phoneNumber
            )
        print("received SMS stored")
    except Exception as e: 
        print(e)
        print("received SMS not stored.")
        return False
    finally:
        return True

def setUrl(phone,message):
    url = 'http://10.8.0.11:7405/SendSMS?username=testing&password=testing123&phone='+phone+'&message='+message
    x = requests.get(url)
    print(x.text)
    try:
        sendSMS.objects.create(
            message = message,
            phoneNo = phone
        )
        print("sent sms stored")
    except Exception as e:
        print(e)
        print("sent sms not stored...")
        return False
    finally:
        return True    
 