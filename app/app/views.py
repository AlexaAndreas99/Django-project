from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# noinspection PyUnresolvedReferences
from login.models import Subject
from .forms import AddGrade


@login_required
def home(request):
    user = request.session.get('user', 'Guest')
    subjects = Subject.objects.all()
    d = ['Geometry', 'Web design', 'Programming']

    context = {'user': user, 'subjects': subjects, 'd': d}
    return render(request, "home.html", context)


@login_required
def add(request):
    form = AddGrade(request.POST or None)
    if form.is_valid():
        form.save()

    context = {'form': form}
    return render(request, "add.html", context)
