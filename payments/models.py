from django.db import models


class Organization(models.Model):
    inn = models.CharField(max_length=12, unique=True, primary_key=True)
    balance = models.DecimalField(max_digits=15, decimal_places=2, default=0)

    class Meta:
        verbose_name = "Организация"
        verbose_name_plural = "Организации"

    def __str__(self):
        return f"Организация {self.inn}"


class Payment(models.Model):
    operation_id = models.UUIDField(unique=True)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    payer_inn = models.CharField(max_length=12)
    document_number = models.CharField(max_length=100)
    document_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Платеж"
        verbose_name_plural = "Платежи"
        ordering = ['-created_at']

    def __str__(self):
        return f"Платеж {self.operation_id} - {self.amount}"


class BalanceLog(models.Model):
    organization = models.ForeignKey(Organization,
                                     on_delete=models.CASCADE,
                                     related_name='logs')
    old_balance = models.DecimalField(max_digits=15, decimal_places=2)
    new_balance = models.DecimalField(max_digits=15, decimal_places=2)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Лог баланса"
        verbose_name_plural = "Логи баланса"
        ordering = ['-created_at']

    def __str__(self):
        return f"Изменени баланса для {self.organization.inn} - {self.old_balance} -> {self.new_balance}"

