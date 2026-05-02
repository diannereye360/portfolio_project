from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Project, ContactMessage
from .forms import ContactForm


def index(request):
    projects = Project.objects.filter(is_active=True)

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            ContactMessage.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                subject=form.cleaned_data['subject'],
                message=form.cleaned_data['message'],
            )
            messages.success(request, "Message received! I'll get back to you soon.")
            return redirect('index')
    else:
        form = ContactForm()

    return render(request, 'main/index.html', {'projects': projects, 'form': form})
