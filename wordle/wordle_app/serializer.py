from rest_framework import serializers

from .models import WordleNames

class WordleNamesSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=5)

    class Meta:
        model = WordleNames
        fields = ('__all__')