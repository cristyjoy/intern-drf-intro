from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Anime, Website, Breeds

# Register your models here.

# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ('url', 'username', 'email', 'groups')

# class GroupSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Group
#         fields = ('url', 'name')


class AnimeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Anime
        fields = ('title', 'description', 'director', 'release_date', 'score', 'picture', 'date_modified', 'date_created')

class WebsiteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Website
        fields = ('name', 'link', 'owner', 'logo', 'date_modified', 'date_created')

class BreedsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Breeds
        fields = ('name', 'description', 'country', 'is_official', 'date_modified', 'date_created')
