from django.shortcuts import render, redirect
from dashboard.models import Message
from django.contrib import messages


# def home(request):
#     return render(request, 'public/home.html')

def contact_page(request):
    if request.method == 'POST':
        Message.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            subject=request.POST['subject'],
            message=request.POST['message']
        )
        messages.success(request, "Message sent successfully!")
        return redirect('contact')

    return render(request, 'public/contact.html')



from dashboard.models import Service

def services_page(request):
    services = Service.objects.filter(is_active=True).order_by('-created_at')
    return render(request, 'public/services.html', {'services': services})


def home(request):
    services = Service.objects.filter(is_active=True)
    return render(request, 'public/home.html', {'services': services})
