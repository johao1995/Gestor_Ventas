from django.contrib import admin
from .models import Cliente

class ClienteAdmin(admin.ModelAdmin):
    list_display=(
        'id',
        'first_name',
        'last_name',
        'city',
        'category',
        'fecha'
    )
admin.site.register(Cliente,ClienteAdmin)