from django.urls import include, path
from apps.accounts.views.sign_up import UserSignUpView


urlpatterns = [
    path('signup/', UserSignUpView.as_view())
]