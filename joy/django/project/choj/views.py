
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from choj.serializers import AnimeSerializer, WebsiteSerializer, BreedsSerializer
from .models import Anime, Website, Breeds

# Create your views here.



class AnimeViewSet(viewsets.ModelViewSet):
    queryset = Anime.objects.all().order_by('-date_created')
    serializer_class = AnimeSerializer

class WebsiteViewSet(viewsets.ModelViewSet):
    queryset = Website.objects.all().order_by('-owner')
    serializer_class = WebsiteSerializer

class BreedsViewSet(viewsets.ModelViewSet):
    queryset = Breeds.objects.all().order_by('-name')
    serializer_class = BreedsSerializer
