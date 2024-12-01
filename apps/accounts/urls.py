from django.urls import include, path
from accounts.views.sign_up import UserSignUpView
# from accounts.views.login import LoginView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('signup/', UserSignUpView.as_view()),
    # path('login/', LoginView.as_view()),
    path('login/', TokenObtainPairView.as_view()),
    path('refresh_token/', TokenRefreshView.as_view())
]