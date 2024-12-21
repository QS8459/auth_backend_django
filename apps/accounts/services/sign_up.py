from accounts.models.user import Users
from rest_framework.response import Response
from rest_framework import status
from accounts.serializers.sign_up import SignUpResponse


def sign_up(email:str, password:str) -> Response:
    check_email =Users.objects.filter(email__iexact = email)
    if check_email.exists() is True:
        if check_email.first().is_active is False:
            return Response({'detail':"Please Activate your Account"}, status = status.HTTP_400_BAD_REQUEST)

        return Response({"detail":"Email already exists"},status = status.HTTP_400_BAD_REQUEST)
    else:
        user = create_user(email, password)
        result = {
            'id': user.id,
            'email': user.email
        }
        return Response({'detail':result}, status = status.HTTP_200_OK)


def create_user(email: str, password: str):
    user =Users.objects.create_user(email)
    if password:
        user.set_password(password)
        user.save()
    return user