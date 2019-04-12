from django.shortcuts import redirect
from .models import Contact
from django.contrib import messages
from django.core.mail import send_mail


def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        # check if user has made inquiry already
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(user_id=user_id)
            if has_contacted:
                messages.error(request, 'inquiry already made')
                return redirect('/listings/'+listing_id)

        contact = Contact(
                            listing_id=listing_id,
                            listing=listing,
                            name=name, email=email, phone=phone,
                            message=message, user_id=user_id
                            )

        contact.save()

        send_mail(
                'Property Inquiry',
                'Inquiry has been made ' + listing + ' .signin for info',
                'maharjansagun121@gmail.com',
                [realtor_email, 'sagunmaharjan121@gmail.com'],
                fail_silently=False
            )

        messages.success(request, 'Inquiry sent')
        return redirect('/listings/'+listing_id)
