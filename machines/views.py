from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, Paginator
from .models import Machine
from .models import Company

def index(request):
    machines = Machine.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(machines, 12)
    page = request.GET.get('page')
    paged_machines = paginator.get_page(page)


    context = {
        'machines': paged_machines
    }
    return render(request, 'machines/machines.html', context)

def machine(request):
    machine = get_object_or_404(Machine, pk=machine_id)
    context={
        'machine' : machine
    }

    return render(request, 'machines/machine.html', context)

def m_search(request):
    queryset_list = Machine.objects.order_by('-list_date')
    
    #name
    if 'machine_name' in request.GET:
       machine_name = request.GET['machine_name']
       if machine_name:
        queryset_list = queryset_list.filter(machine_name__icontains=machine_name)
       
    if 'company' in request.GET:
      company = request.GET['company']
      if company:
       queryset_list = queryset_list.filter(company__icontains=company)

    if 'operator_name' in request.GET:
      operator_name = request.GET['operator_name']
      if operator_name:
       queryset_list = queryset_list.filter(operator_name__icontains=operator_name)




    if 'licence_no' in request.GET:
      licence_no = request.GET['licence_no']
      if licence_no:
       queryset_list = queryset_list.filter(licence_no__icontains=licence_no)

    if 'comment' in request.GET:
      comment = request.GET['comment']
      if comment:
       queryset_list = queryset_list.filter(comment__icontains=comment)


    if 'licence_expiry' in request.GET:
      licence_expiry = request.GET['licence_expiry']
      if licence_expiry:
       queryset_list = queryset_list.filter(licence_expiry__icontains=licence_expiry)

    context= {
        'machines': queryset_list,
        'values': request.GET
}


    return render(request, 'machines/m_search.html', context)