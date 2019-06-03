from rest_framework import serializers
from sigs.models import Sig


class SigSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Sig
