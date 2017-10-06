from rest_framework import serializers
from .models import Member


class MemberSerializer(serializers.HyperlinkedModelSerializer):
    email = serializers.CharField(default="")
    name = serializers.CharField(default="")
    password = serializers.CharField(default="")

    class Meta:
        model = Member
        fields = ('email', 'name', 'password')