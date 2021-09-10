from django.contrib import admin
from .models import App, Subscription, Plan
# Register your models here.

@admin.register(App)
class AppAdmin(admin.ModelAdmin):
    list_display = ["name","type","domain_name","framework"]
    search_fields = ['name']
    
    
@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "description"]
    search_fields = ['name']
    
    
@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = [ "user", "plan", "app",]
    
    