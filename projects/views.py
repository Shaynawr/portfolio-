from django.shortcuts import render_to_response
from django.core.mail import send_mail
# Create your views here.


def send_contact(request):
    email = request.POST.get('email')
    name = request.POST.get('name')
    phone = request.POST.get('phone')
    message = request.POST.get('message')
    print "Email: %s" % email

    email_message = "The following message was sent from '%s' <%s>, phone number %s:\n\n%s" %(name, email, phone, message)

    send_mail('Contact Form on Portfolio', email_message, email, ['shaynawr@gmail.com'])

    return render_to_response('contact_success.html')