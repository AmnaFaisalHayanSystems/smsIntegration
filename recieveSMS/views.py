from rest_framework import (
    #generics,
    views,
    #filters,
    status
)
# from rest_framework.permissions import IsAuthenticated
# from rest_framework_simplejwt import authentication
from rest_framework.response import Response

from recieveSMS.utils import storeMessage
from recieveSMS.utils import setUrl
import json

class SMSreceiverAPI(views.APIView):
    def get(self,request):
        """Just a GET request view for testing purposes"""
        phoneNumber = request.query_params.get("phoneNumber", None)
        if phoneNumber:
            message = request.query_params.get("message", None)
            if message:
                if storeMessage(phoneNumber,message):
                    return Response(status=status.HTTP_200_OK,
                    data = json.dumps("Message recieved and stored")
                    )
                else:
                    return Response(status=status.HTTP_400_BAD_REQUEST,
                    data = json.dumps("Message recieved but not stored")
                    )
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST,
                data = json.dumps("missing message parametre")
                )
        else:

            return Response(status=status.HTTP_400_BAD_REQUEST,
            data = json.dumps("missing phoneNumber parametre")
            )

class SMSsenderAPI(views.APIView):
    def get(self,request):
        """Just a GET request view for testing purposes"""
        phoneNumber = request.query_params.get("phoneNumber", None)
        if phoneNumber:
            message = request.query_params.get("message", None)
            if message:
                return Response(status=status.HTTP_200_OK,
                data = json.dumps(setUrl(phoneNumber,message))
                )
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST,
                data = json.dumps("missing message parametre")
                )
        else:

            return Response(status=status.HTTP_400_BAD_REQUEST,
            data = json.dumps("missing phoneNumber parametre")
            )