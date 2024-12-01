from rest_framework import serializers

class LoginSerializer(serializers.Serializer):
    email:str = serializers.EmailField()
    password:str = serializers.CharField(max_length=200)

