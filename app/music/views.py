from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .models import Artiste, Chanson
from .serializers import ArtisteSerializer, ChansonSerializer
from rest_framework.response import Response

# Create your views here.
class ArtisteAPIView(APIView):
    def get(self, *args, **kwargs):
        artiste = Artiste.objects.all()
        serializer = ArtisteSerializer(artiste, many=True)
        return Response(serializer.data)

class ChansonsListAPIView(APIView):
    def get(self, *args, **kwargs):
        chanson = Chanson.objects.values_list('titre', flat=True)
        return Response(data={"chansons": chanson})

class ArtisteViewSet(ModelViewSet):
    serializer_class = ArtisteSerializer
    
    def get_queryset(self):
        queryset = Artiste.objects.all()

        styleParam = self.request.GET.get("style")
        nameParam = self.request.GET.get("nom")

        if nameParam is not None:
            queryset = queryset.filter(nom=nameParam)

        if styleParam is not None:
            queryset = queryset.filter(style=styleParam)

        return queryset

class ChansonViewSet(ModelViewSet):
    serializer_class = ChansonSerializer
    
    def get_queryset(self):
        return Chanson.objects.all()