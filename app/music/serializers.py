from rest_framework import serializers
from .models import Artiste, Chanson

class ChansonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Chanson
        fields = ["id", "titre", "durée", "date", "artiste"]

class ArtisteSerializer(serializers.ModelSerializer):

    chansons = ChansonSerializer(many=True)

    class Meta:
        model = Artiste
        fields = ["id", "nom", "style", "chansons"]
