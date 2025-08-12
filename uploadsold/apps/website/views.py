from django.shortcuts import render

# Create your views here.


def Home(request):  
    context = {}

    return render(request, 'website/index.html', context)



def About(request):  
    context = {}

    return render(request, 'website/about_us.html', context)



