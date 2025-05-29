from django.contrib import admin
from .models import Payment, BalanceLog, Organization

@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('inn', 'balance')
    search_fields = ('inn',)


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('operation_id', 'amount', 'payer_inn', 'document_number', 'document_date', 'created_at')
    list_filter = ('document_date', 'created_at', 'payer_inn')
    search_fields = ('operation_id', 'payer_inn', 'document_number')


@admin.register(BalanceLog)
class BalanceLogAdmin(admin.ModelAdmin):
    list_display = ('organization', 'amount', 'old_balance',
                   'new_balance', 'created_at', 'payment', 'created_at')
    list_filter = ('created_at', 'organization')
    search_fields = ('organization__inn', 'payment__document_number')
