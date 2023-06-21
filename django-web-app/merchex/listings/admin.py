from django.contrib import admin
from listings.models import Account

# Register your models here.
class AccountAdmin(admin.ModelAdmin):
    list_display = ('group', 'name', 'email', 'password')

admin.site.register(Account, AccountAdmin)
