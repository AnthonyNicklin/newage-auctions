from django.contrib import admin

from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):

    model = OrderLineItem


class OrderAdmin(admin.ModelAdmin):

    inlines = (OrderLineItemAdminInline, )

admin.site.register(Order, OrderAdmin)
