from django.urls import path

from recieveSMS.views import SMSreceiverAPI
# from recieveSMS.views import SMSsenderAPI

urlpatterns = [
    path('ReceiveSMS',SMSreceiverAPI.as_view()),
    # path('SendSMS',SMSsenderAPI.as_view()),
]


