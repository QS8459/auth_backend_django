from rest_framework import serializers
from accounts.models.user import Users
class SignUpSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

class SignUpResponse(serializers.Serializer):
    class Meta:
        model = Users
        fields = '__all__'

