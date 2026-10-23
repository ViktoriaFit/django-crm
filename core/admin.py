from django.contrib import admin
from .models import Client
from datetime import date
from django.utils.safestring import mark_safe

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = (
        'last_name', 
        'phone', 
        'visits', 
        'payment_date', 
        'start_date', 
        'expiry_date', 
        'days_of_week', 
        'training_time',
        'status_colored'
    )
    search_fields = ('last_name', 'phone')

    def status_colored(self, obj):
        today = date.today()
        days_left = (obj.expiry_date - today).days

        if days_left < 0:
            color = '#e74c3c'
            text = f"❌ ПРОСРОЧЕН (с {obj.expiry_date})"
        elif days_left <= 5:
            color = '#f1c40f'
            text = f"⚠️ Скоро конец ({obj.expiry_date})"
        else:
            color = '#27ae60'
            text = f"✅ Действует до {obj.expiry_date}"
        
        return mark_safe(f'<span style="color: {color}; font-weight: bold;">{text}</span>')

    status_colored.short_description = "Статус"
    status_colored.allow_tags = True

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.order_by('expiry_date')