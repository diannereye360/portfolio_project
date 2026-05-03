from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Project, ContactMessage, Skill
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


def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk, is_active=True)
    tools = [t.strip() for t in project.tools_used.splitlines() if t.strip()]
    features = [f.strip() for f in project.key_features.splitlines() if f.strip()]
    return render(request, 'main/project_detail.html', {
        'project': project,
        'tools': tools,
        'features': features,
    })


def skills(request):
    all_skills = Skill.objects.all()
    categories = {}
    for skill in all_skills:
        categories.setdefault(skill.category, []).append(skill)
    return render(request, 'main/skills.html', {'categories': categories})


def resume(request):
    return render(request, 'main/resume.html')
