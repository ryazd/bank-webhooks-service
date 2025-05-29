from rest_framework import serializers
from .models import Organization, Payment


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['operation_id', 'amount', 'payer_inn', 'document_number', 'document_date']


class BalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ['inn', 'balance']