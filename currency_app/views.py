import json
import requests
import time
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CurrencyRequest
from .serializers import CurrencyRequestSerializer


class GetCurrentUSDView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            last_request_timestamp = request.session.get("last_request_timestamp")

            if last_request_timestamp and (time.time() - last_request_timestamp) < 10:
                time.sleep(10)

            response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
            response.raise_for_status()
            data = response.json()
            usd_to_rub_rate = data["rates"]["RUB"]

            try:
                CurrencyRequest.objects.create(rate=usd_to_rub_rate)
            except IntegrityError:
                pass

            request.session["last_request_timestamp"] = time.time()

            last_requests = CurrencyRequest.objects.all()[:10]
            serializer = CurrencyRequestSerializer(last_requests, many=True)

            response_data = {
                "usd_to_rub_rate": usd_to_rub_rate,
                "last_requests": serializer.data,
            }

            return Response(response_data)

        except requests.exceptions.RequestException as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
