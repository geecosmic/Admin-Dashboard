from django.contrib import admin
from .models import Message
from .models import Service

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'is_read', 'created_at')
    list_filter = ('is_read',)





# @admin.register(Service)
# class ServiceAdmin(admin.ModelAdmin):
#     list_display = ('title', 'is_active', 'created_at')
#     list_filter = ('is_active',)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'created_at')
    fields = ('title', 'description', 'image', 'is_active')
