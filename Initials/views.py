from django.shortcuts import render


# Create your views here.
def InitialSite(request):


    return render(request, 'Initial HTML/index.html')