from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from accounts.services.sign_up import sign_up
from accounts.serializers.sign_up import SignUpSerializer

class UserSignUpView(APIView):
    serializer_class = SignUpSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = self.serializer_class(data = request.data)
        serializer.is_valid(raise_exception=True)
        return sign_up(**serializer.validated_data)