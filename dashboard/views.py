from django.shortcuts import render

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Message
from django.contrib.auth.models import User


from .models import Service
from django.contrib import messages

from django.db.models import Q


from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def dashboard_home(request):
    context = {
        'total_messages': Message.objects.count(),
        'unread_messages': Message.objects.filter(is_read=False).count(),
        'total_services': Service.objects.count(),
        'active_services': Service.objects.filter(is_active=True).count(),
        'total_users': User.objects.count(),
    }
    return render(request, 'dashboard/home.html', context)




# @login_required
# def message_list(request):
#     messages = Message.objects.order_by('-created_at')
#     return render(request, 'dashboard/messages_list.html', {'messages': messages})


@login_required
def message_list(request):
    messages = Message.objects.order_by('-created_at')

    q = request.GET.get('q')
    status = request.GET.get('status')

    if q:
        messages = messages.filter(
            Q(name__icontains=q) |
            Q(email__icontains=q) |
            Q(subject__icontains=q)
        )

    if status == 'read':
        messages = messages.filter(is_read=True)
    elif status == 'unread':
        messages = messages.filter(is_read=False)

    return render(request, 'dashboard/messages_list.html', {
        'messages': messages
    })







@login_required
def message_detail(request, pk):
    message = get_object_or_404(Message, pk=pk)
    message.is_read = True
    message.save()
    return render(request, 'dashboard/message_detail.html', {'message': message})


@login_required
def mark_message_read(request, msg_id):
    msg = get_object_or_404(Message, id=msg_id)
    msg.is_read = True
    msg.save()
    return redirect('messages_list')


@login_required
def message_delete(request, pk):
    message = get_object_or_404(Message, pk=pk)
    message.delete()
    return redirect('message_list')




@login_required
def service_list(request):
    services = Service.objects.order_by('-created_at')
    return render(request, 'dashboard/service_list.html', {'services': services})




@login_required
def service_create(request):
    if request.method == 'POST':
        image = request.FILES.get('image')  # Get uploaded image if any
        Service.objects.create(
            title=request.POST['title'],
            description=request.POST['description'],
            is_active=request.POST.get('is_active') == 'on',
            image=image
        )
        messages.success(request, 'Service created successfully')
        return redirect('service_list')

    return render(request, 'dashboard/service_form.html')


@login_required
def service_edit(request, pk):
    service = get_object_or_404(Service, pk=pk)

    if request.method == 'POST':
        service.title = request.POST['title']
        service.description = request.POST['description']
        service.is_active = request.POST.get('is_active') == 'on'
        image = request.FILES.get('image')
        if image:  # Update only if a new image is uploaded
            service.image = image
        service.save()
        messages.success(request, 'Service updated successfully')
        return redirect('service_list')

    return render(request, 'dashboard/service_form.html', {'service': service})


# @login_required
# def service_create(request):
#     if request.method == 'POST':
#         Service.objects.create(
#             title=request.POST['title'],
#             description=request.POST['description'],
#             is_active=request.POST.get('is_active') == 'on'
#         )
#         messages.success(request, 'Service created successfully')
#         return redirect('service_list')

#     return render(request, 'dashboard/service_form.html')


# @login_required
# def service_edit(request, pk):
#     service = get_object_or_404(Service, pk=pk)

#     if request.method == 'POST':
#         service.title = request.POST['title']
#         service.description = request.POST['description']
#         service.is_active = request.POST.get('is_active') == 'on'
#         service.save()
#         messages.success(request, 'Service updated successfully')
#         return redirect('service_list')

#     return render(request, 'dashboard/service_form.html', {'service': service})


@login_required
def toggle_service(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    service.is_active = not service.is_active
    service.save()
    return redirect('services_list')



@login_required
def service_delete(request, pk):
    service = get_object_or_404(Service, pk=pk)
    service.delete()
    messages.success(request, 'Service deleted')
    return redirect('service_list')



