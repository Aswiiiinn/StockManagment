from django.contrib import admin
from .models import Stocks
from .forms import Stockforms

class stockFormAdmin(admin.ModelAdmin):
    list_display = ['categories', 'item_name', 'quantity','created_by']
    form = Stockforms
    list_filter = ['categories']
    search_fields = ['item_name']

admin.site.register(Stocks, stockFormAdmin)
