from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    #return HttpResponse("This is our first client page")

    context_dict = {'app_description': "This is your client app, where you can manage your account clients"}

    return render(request, 'clients/index.html', context_dict)