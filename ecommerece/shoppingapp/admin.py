from django.contrib import admin
from shoppingapp.models import section , product ,detailing ,Cart,completeorder
# Register your models here.

admin.site.register(section)
admin.site.register(product)
admin.site.register(detailing)
admin.site.register(completeorder)
class add_admin_view(admin.ModelAdmin):
    list_display= 'user','product'

admin.site.register(Cart,add_admin_view)