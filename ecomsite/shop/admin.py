from django.contrib import admin
from .models import Products, Order
# Register your models here.

admin.site.site_header = "E-commerce Site"
admin.site.site_title = "Shopping"
admin.site.index_title = "Manage Shopping"

class ProductAdmin(admin.ModelAdmin):

    def change_category_to_default(self, request, queryset):
        queryset.update(prodCategory="Default")
    
    change_category_to_default.short_description = 'Change to Default Category'
    list_display = ('prodTitle', 'prodPrice')
    search_fields = ('prodTitle', 'prodCategory',)
    actions = ('change_category_to_default',)
    fields = ('prodTitle', 'prodPrice',)
    list_editable = ('prodPrice',)

admin.site.register(Products, ProductAdmin)
admin.site.register(Order)

