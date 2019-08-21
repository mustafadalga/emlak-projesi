from django.shortcuts import render,redirect
from .models import Contact
from django.contrib import messages
from django.core.mail import send_mail
# Create your views here.

def contact(request):
    if request.method=="POST":
        listing_id=request.POST['listing_id']
        listing=request.POST['listing']
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        message=request.POST['message']
        user_id=request.POST['user_id']
        realtor_email=request.POST['realtor_email']


        #Mesajın gönderilip gönderilmediğini kontrol et
        if request.user.is_authenticated:
            user_id=request.user.id
            has_contacted=Contact.objects.all().filter(listing_id=listing_id,user_id=user_id)
            if has_contacted:
                messages.error(request,'İletiniz emlakçıya zaten gönderildi!')
                return redirect('/listings/' + listing_id)


        contact=Contact(listing=listing,listing_id=listing_id,name=name,email=email,phone=phone,message=message,user_id=user_id)


        contact.save()

        #Email Gönderme

        send_mail(
            listing+ ' emlağınız için bir bildirim var!',
            listing+' emlağınız için bir tane ileti geldi.Daha fazla bilgi için yönetim paneline bakınız',
            'djangoicin@gmail.com',
            [realtor_email,'mustafadalgaa@gmail.com'],
            fail_silently=False

        )



        messages.success(request,'İletiniz emlakçıya gönderildi.Yakında dönüş alacaksınız')

        return redirect('/listings/'+listing_id)


