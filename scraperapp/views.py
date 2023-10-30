from django.http import HttpResponseRedirect
from django.shortcuts import render
from bs4 import BeautifulSoup
import requests

from .models import Link


# Create your views here.
def home(request):
    if request.method == 'POST':
        newlink = request.POST.get('page', '')
        urls = requests.get(newlink)
        bsoup = BeautifulSoup(urls.text, 'html.parser')
        listsoup = []

        for i in bsoup.findAll('a'):
            # listsoup.append(i.get('href'))
            liaddress = i.get('href')
            liname = i.string
            Link.objects.create(address=liaddress, stringname=liname)

        return HttpResponseRedirect('/')

    else:
        data_values = Link.objects.all()

    return render(request, 'home.html', {'data_values': data_values})
