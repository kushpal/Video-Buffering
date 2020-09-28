from rest_framework import serializers

from .models import Video

class VideoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'


class VideoPath(object): 
    def __init__(self, dictionary): 
        self.dictionary = dictionary 
  
# create a serializer 
class VideoPathSerializer(serializers.Serializer): 
    # intialize fields 
    dictionary = serializers.DictField(child = serializers.CharField()) 
      
