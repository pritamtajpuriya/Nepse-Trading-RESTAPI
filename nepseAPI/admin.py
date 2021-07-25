from django.contrib import admin
from .models import *

# Register your models here.

class TradeAdminConfig(admin.ModelAdmin):
    list_display = ['symbol','ltp','change','high','low']
 
class CompanyAdminConfig(admin.ModelAdmin):
    list_display = ['name','trade','sector','market_price','eps']
admin.site.register(Trade,TradeAdminConfig)

admin.site.register(Company,CompanyAdminConfig)