from django.contrib import admin

from .models import MenuItem, Order, Table, Reservation, Inventory
from .forms import ReservationForm
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description')
    search_fields = ('name', 'description')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('menu_item_name', 'menu_item_price','quantity', 'order_date')
    search_fields = ('menu_item__name',)
    list_filter = ('order_date',)

class TableAdmin(admin.ModelAdmin):
    list_display = ('table_number', 'seats', 'status')
    search_fields = ('table_number',)
    list_filter = ('status',)

class ReservationAdmin(admin.ModelAdmin):
    form = ReservationForm
    list_display = ('table', 'reservation_name', 'reservation_phone', 'reservation_date')
    search_fields = ('reservation_name', 'reservation_phone')
    list_filter = ('reservation_date',)

class InventoryAdmin(admin.ModelAdmin):
    list_display = ('item_name', 'item_quantity', 'price', 'total_price')
    search_fields = ('item_name',)


admin.site.register(MenuItem, MenuItemAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Table, TableAdmin)
admin.site.register(Reservation, ReservationAdmin)
admin.site.register(Inventory, InventoryAdmin)