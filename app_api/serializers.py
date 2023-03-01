from rest_framework import serializers
from my_app.models import ServerImages

class ServerImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ServerImages
        fields = '__all__'
