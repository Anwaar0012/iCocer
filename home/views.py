from django.shortcuts import render, HttpResponse
from home.models import Contact
from django.contrib import messages

# Create your views here.
def home(request): 
    return render(request,'home/home.html')



def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        content =request.POST['content']
        # data base mein dalna Contact model ka obj
        contact=Contact(name=name, email=email, phone=phone, content=content)
        # showing messages 
        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<4:
            messages.error(request, "Please fill the form correctly")
        else:
            contact=Contact(name=name, email=email, phone=phone, content=content)
            # is obj ko data base mein save kardo
            contact.save()
            messages.success(request, "Your message has been successfully sent")
        
        
    #  render contact.html     # 
    return render(request, "home/contact.html")

def search(request):
    query=request.GET['query']
    allPosts= Post.objects.filter(title__icontains=query)
    params={'allPosts': allPosts}
    return render(request, 'home/search.html', params)


def about(request): 
    return render(request,'home/about.html')
