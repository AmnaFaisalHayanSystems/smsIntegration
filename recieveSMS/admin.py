from django.contrib import admin

# Register your models here.
# TODO: @AMNA
from recieveSMS.models import SMSstorage
from recieveSMS.models import sendSMS

# TODO: @AMNA
admin.site.register(SMSstorage)
admin.site.register(sendSMS)
