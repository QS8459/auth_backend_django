from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from accounts.serializers.login import LoginSerializer

from accounts.services.login import login
class LoginView(APIView):
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data = request.data)
        serializer.is_valid(raise_exception=True)
        return login(**serializer.validated_data)