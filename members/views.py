import json
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from .models import Member
from .serializer import MemberSerializer


@csrf_exempt
@api_view(['GET', 'POST'])
def member_list(request):
    if request.method == 'GET':
        serializer = MemberSerializer(Member.objects.all(), many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        print (data['name'])
        serializer = MemberSerializer(Member.objects.filter(name=data['name']), many=True)
        return Response(serializer.data)