from rest_framework import status
from rest_framework.response import Response
from accounts.backends import EmailBackend


def login(email:str = None, password:str = None) -> Response:
    servicer = EmailBackend()
    user = servicer.authenticate(email, password)
    return_user = {
        'id': user.id,
        'email': user.email
    }
    if user:
        return Response({'results':return_user},status = status.HTTP_200_OK)

    return Response({'detail':"Wrong response"}, status = status.HTTP_404_NOT_FOUND)