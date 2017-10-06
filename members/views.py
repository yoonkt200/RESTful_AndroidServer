from django.shortcuts import render
from rest_framework import viewsets
from .models import Member
from .serializer import MemberSerializer


class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer