
from django.shortcuts import redirect, render
from django.urls import reverse

from .models import Brand,Feature, Person,Rating,Project
from .forms import RequestForm

def home_view(request):
    brands = Brand.objects.all()
    features = Feature.objects.all()
    ratings = Rating.objects.all()
    projects = Project.objects.all()

    data = {
        'brands': brands,
        'features':features,
        'ratings': ratings,
        'projects': projects
    }

    return render(request,'main/home.html',context=data)

def contact_us_view(request):
    return render(request,'main/contact.html')

def success_view(request):
    return render(request,'main/success.html')

def about_us_view(request):
    persons = Person.objects.all()
    data = {
        'persons': persons
    }
    return render(request,'main/about-us.html',context=data)

def projects_view(request):
    projects = Project.objects.all()
    data = {
        'projects': projects
    }
    return render(request,'main/projects.html',context=data)

def submit_request(request):

    if request.method == "POST" or None:
        form = RequestForm(request.POST or None)
        if  form.is_valid():
            form.save(commit=False)
            print("Valid Form")
            form.save()
            return redirect(reverse('success_view'))
        else:
            return render(request, 'main/contact.html',{'form':form})
    else:
        return render(request, 'main/404.html')

    