from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import Account
from userauths.models import User

# Register your models here.

class AccountAdminModel(ImportExportModelAdmin):
    list_editable = ['account_status', 'account_balance']
    list_display = ['user', 'account_number', 'account_status', 'account_balance']
    list_filter = ['account_status']

admin.site.register(Account,AccountAdminModel)
