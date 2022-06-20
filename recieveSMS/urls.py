from django.urls import path

from recieveSMS.views import SMSreceiverAPI
urlpatterns = [
    path('ReceiveSMS',SMSreceiverAPI.as_view()),
    
]