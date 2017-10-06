from rest_framework import serializers
from .models import Member


class MemberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Member
        fields = ('email', 'name', 'password')