from django.contrib import admin
from services.models import Customer,Services,Appointment

# Register your models here.
@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('sp_name','providing_services',)
    ordering = ('sp_name',)
    search_fields = ('sp_name','providing_services',)
    list_filter = ('sp_name', 'providing_services',)
    
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('c_name','c_email',)
    ordering = ('c_name',)
    search_fields = ('c_name','c_email',)
    list_filter = ('c_name', 'c_email',)

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('customer','services','a_date',)
    ordering = ('customer',)
    search_fields = ('customer','services','a_date',)
    list_filter = ('customer', 'services','a_date',)
    
