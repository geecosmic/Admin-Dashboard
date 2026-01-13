from django.urls import path

from .views import login_view, logout_view, register_view, user_list,toggle_user_active,delete_user


urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('users/', user_list, name='user_list'),
    path('users/<int:user_id>/toggle/', toggle_user_active, name='toggle_user'),
    path('users/<int:user_id>/delete/', delete_user, name='delete_user'),


]
