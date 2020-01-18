from django.contrib import admin

from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    
    model = OrderLineItem


class OrderAdmin(admin.ModelAdmin):

    readonly_fields = ('payment_id', 'date')
    inlines = (OrderLineItemAdminInline, )

admin.site.register(Order, OrderAdmin)
