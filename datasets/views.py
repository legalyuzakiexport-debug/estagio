from django.shortcuts import render

def dashboard(request):
    return render(request, 'frontend/dashboard.html')

def datasets(request):
    return render(request, 'frontend/datasets.html')

def login_view(request):
    return render(request, 'frontend/login.html')

def register_view(request):
    return render(request, 'frontend/register.html')

def dataset_create(request):
    return render(request, 'frontend/dataset_create.html')

def dataset_detail(request, id):
    return render(request, 'frontend/dataset_detail.html', {'dataset_id': id})
