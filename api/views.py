from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import RandomKey
import uuid

class KeyHome(APIView):
    def get(self, request):
        uid = uuid.uuid1()
        new_id = uid.hex
        RandomKey.objects.create(
            uid = new_id
        )
        keys = RandomKey.objects.order_by("pk").reverse()
        data = []
        for key in keys:
            datas = {
                "key": key.date,
                "uuid": key.uid
            }
            data.append(datas)
        return Response(data, status=status.HTTP_200_OK)
