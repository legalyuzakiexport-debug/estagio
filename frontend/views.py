from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    return render(request, 'frontend/dashboard.html')

def datasets(request):
    return render(request, 'frontend/datasets.html')

def login_view(request):
    return render(request, 'frontend/login.html')

def register_view(request):
    return render(request, 'frontend/register.html')

@login_required
def dataset_detail(request, id):
    return render(request, 'frontend/dataset_detail.html', {'dataset_id': id})

@login_required
def dataset_create(request):
    return render(request, 'frontend/dataset_create.html')

def categories(request):
    return render(request, 'frontend/categories.html')

@login_required
def profile(request):
    return render(request, 'frontend/profile.html')