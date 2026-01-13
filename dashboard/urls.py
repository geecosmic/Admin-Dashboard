from django.urls import path
from .views import (
    dashboard_home,
    message_list,
    message_detail,
    message_delete,
    service_list,
    service_create,
    service_edit,
    service_delete,
    mark_message_read,
    toggle_service,
)

urlpatterns = [
    path('', dashboard_home, name='dashboard_home'),
    path('messages/', message_list, name='message_list'),
    path('messages/<int:pk>/', message_detail, name='message_detail'),
    path('messages/<int:msg_id>/read/', mark_message_read, name='mark_message_read'),

    path('messages/<int:pk>/delete/', message_delete, name='message_delete'),

    path('services/', service_list, name='service_list'),
    path('services/create/', service_create, name='service_create'),
    path('services/<int:service_id>/toggle/',toggle_service, name='toggle_service'),

    path('services/<int:pk>/edit/', service_edit, name='service_edit'),
    path('services/<int:pk>/delete/', service_delete, name='service_delete'),
]
