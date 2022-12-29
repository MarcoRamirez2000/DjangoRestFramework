from rest_framework.serializers import ModelSerializer 
from AppRestFramework.models import Post

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields =  ['id','content']