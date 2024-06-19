from django.urls import path

from . import views

app_name = "account"

urlpatterns = [
    path('kyc-reg/', views.kyc_registration, name='kyc-reg'),
]
