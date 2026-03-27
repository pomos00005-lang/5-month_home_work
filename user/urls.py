from django.urls import path
from . import views

urlpatterns = [
    path('registration/',views.RegistrationAPIView.as_view()),
    path('registration/confirm/',views.ConfirmAuthAPIView.as_view()),
    path('authenticate/',views.AuthorizationAPIView.as_view())
]