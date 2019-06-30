from django.shortcuts import render

def index(request):
    return render(request, 'companies/companies.html')

def company(request):
    return render(request, 'companies/company.html')

def search(request):
    return render(request, 'companies/search.html')