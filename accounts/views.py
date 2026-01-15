from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404



@login_required
def register_view(request):
    if not request.user.is_superuser:
        messages.error(request, 'You are not allowed to access this page')
        return redirect('dashboard_home')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
        else:
            user = User.objects.create_user(
                username=username,
                password=password,
                is_staff=True
            )
            messages.success(request, 'User registered successfully')
            return redirect('dashboard_home')

    return render(request, 'accounts/register.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard_home')
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'accounts/login.html')



@login_required
def user_list(request):
    users = User.objects.all().order_by('username')
    return render(request, 'accounts/user_list.html', {'users': users})



@login_required
def toggle_user_active(request, user_id):
    if not request.user.is_superuser:
        messages.error(request, "Permission denied")
        return redirect('dashboard_home')

    user = get_object_or_404(User, id=user_id)

    if user == request.user:
        messages.error(request, "You cannot deactivate yourself")
    else:
        user.is_active = not user.is_active
        user.save()
        messages.success(request, "User status updated")

    return redirect('user_list')


@login_required
def delete_user(request, user_id):
    if not request.user.is_superuser:
        messages.error(request, "Permission denied")
        return redirect('dashboard_home')

    user = get_object_or_404(User, id=user_id)

    if user == request.user:
        messages.error(request, "You cannot delete yourself")
    else:
        user.delete()
        messages.success(request, "User deleted successfully")

    return redirect('user_list')














def logout_view(request):
    logout(request)
    return redirect('login')
