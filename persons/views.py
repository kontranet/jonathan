from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, Paginator
from .models import Person
from companies.models import Company

def index(request):
    persons = Person.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(persons, 12)
    page = request.GET.get('page')
    paged_persons = paginator.get_page(page)


    context = {
        'persons': paged_persons
    }
    return render(request, 'persons/persons.html', context)

def person(request, person_id):
    person = get_object_or_404(Person, pk=person_id)
    context={
        'person' : person
    }
    return render(request, 'persons/person.html', context)


def search(request):
    queryset_list = Person.objects.order_by('-list_date')

    #name
    if 'name' in request.GET:
       name = request.GET['name']
       if name:
        queryset_list = queryset_list.filter(name__icontains=name)
       
    # Name
    if 'company' in request.GET:
      company = request.GET['company']
      if company:
       queryset_list = queryset_list.filter(company__icontains=company)



# Name

    if 'bloodtype' in request.GET:
      bloodtype = request.GET['bloodtype']
      if bloodtype:
       queryset_list = queryset_list.filter(bloodtype__icontains=bloodtype)

# Name
    if 'dateofbirth' in request.GET:
      dateofbirth = request.GET['dateofbirth']
      if dateofbirth:
       queryset_list = queryset_list.filter(dateofbirth__icontains=dateofbirth)

    context= {
        'persons': queryset_list,
        'values': request.GET

}
    return render(request, 'persons/search.html', context)
