from django.contrib import admin
from .models import formatedData


@admin.register(formatedData)
class formatedDataAdmin(admin.ModelAdmin):
    
    list_display = [
        'name',
        'cnic',
        'contactNumber',
        'email',
        'createdAt'
    ]

    search_fields = [
        'name',
        'cnic',
        'contactNumber',
        'email'
    ]