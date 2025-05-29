from django.urls import path
from .views import BankWebhookView, OrganizationBalanceView

urlpatterns = [
    path('webhook/bank/', BankWebhookView.as_view(), name='bank-webhook'),
    path('organizations/<str:inn>/balance/', OrganizationBalanceView.as_view(), name='organization-balance'),
]