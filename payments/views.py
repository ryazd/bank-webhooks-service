from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Organization, Payment, BalanceLog
from .serializers import PaymentSerializer, BalanceSerializer
import logging

logger = logging.getLogger(__name__)


class BankWebhookView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = PaymentSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        data = serializer.validated_data
        operation_id = data['operation_id']

        # Проверка на дубликат платежа
        if Payment.objects.filter(operation_id=operation_id).exists():
            return Response({"detail": "Платеж уже обработан"}, status=status.HTTP_200_OK)

        # Получаем или создаем организацию
        organization, created = Organization.objects.get_or_create(
            inn=data['payer_inn'],
            defaults={'balance': 0}
        )

        # Создаем платеж
        payment = Payment.objects.create(**data)

        # Обновляем баланс
        old_balance = organization.balance
        organization.balance += data['amount']
        organization.save()

        # Логируем изменение баланса
        BalanceLog.objects.create(
            organization=organization,
            old_balance=old_balance,
            new_balance=organization.balance,
            amount=data['amount'],
            payment=payment
        )

        logger.info(
            f"Обновлен баланс для организации {organization.inn}. "
            f"Старый баланс: {old_balance}, Новый баланс: {organization.balance}, "
            f"Сумма: {data['amount']}"
        )

        return Response({"detail": "Платеж успешно обработан"}, status=status.HTTP_200_OK)


class OrganizationBalanceView(APIView):
    def get(self, request, inn, *args, **kwargs):
        organization = get_object_or_404(Organization, inn=inn)
        serializer = BalanceSerializer(organization)
        return Response(serializer.data)