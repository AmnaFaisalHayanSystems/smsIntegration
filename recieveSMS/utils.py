# from recieveSMS.models import SMSstorage
# from recieveSMS.models import sendSMS
import requests
from django.conf import settings


def storeMessage(_phoneNumber , _message):
    # try:
    #     SMSstorage.objects.create(
    #         full_text = _message,
    #         phoneNumber = _phoneNumber
    #         )
    #     print("received SMS stored")
    # except Exception as e: 
    #     print(e)
    #     print("received SMS not stored.")
    #     return False
    # finally:
    return True