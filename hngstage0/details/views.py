from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime, timezone
from decouple import config
import requests

# Create your views here.
@api_view(['GET'])
def me_view(request):
    CAT_FACT_URL = config("CAT_FACT_URL")

    try:
        response = requests.get(CAT_FACT_URL)
        response.raise_for_status()
        fact = response.json().get("fact", "Cat facts are awesome!")

    except requests.RequestException as e:
        fact = "Cat facts are currently unavailable."

    data={
        "status": "success",
        "user": {
            "email": config("EMAIL"),
            "name": config("NAME"),
            "stack": config("STACK")
        },
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "fact": fact
    }
    return Response(data, status=status.HTTP_200_OK, content_type="application/json")