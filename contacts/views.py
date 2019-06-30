from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact

def contact(request):
  if request.method == 'POST':
    person_id = request.POST['person_id']
    c_name = request.POST['c_name']
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    message = request.POST['message']
    user_id = request.POST['user_id']
    # company_email = request.POST['company_email']

    #  Check if user has made inquiry already
    if request.user.is_authenticated:
      user_id = request.user.id
      has_contacted = Contact.objects.all().filter(person_id=person_id, user_id=user_id)
    return redirect('/persons/'+person_id)

    contact = Contact(c_name=c_name, person_id=person_id, name=name, email=email, phone=phone, message=message, user_id=user_id )

    contact.save()

   
    

    messages.success(request, 'Your request has been submitted')
    return redirect('/persons/'+person_id)
