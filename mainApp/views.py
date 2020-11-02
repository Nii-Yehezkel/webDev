# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from requests.auth import HTTPBasicAuth
from django.shortcuts import render, redirect

import requests
import json


# Create views here.
def home_view(request):
    if request.method == 'POST':
        url = 'https://films.dalexapps.com/FilmsWeb/api/web/loginuser'
        username = request.POST.get('Username')
        password = request.POST.get('Password')
        headers = {'Content-Type': 'application/json'}
        LogUser = requests.post(url+'?username='+username+'&'+'password='+password, headers = headers)
        print(LogUser.content)
        return redirect('loanprofile')
    return render(request, 'mainApp/weblinq.html')

def getId():
    url = 'https://films.dalexapps.com/FilmsWeb/api/web/getloanrequest'
    id = request.GET.get('LoanID')
    #id = '6'
    headers = {'Content-Type': 'application/json'}
    LoanProfile = requests.get(url+'?id='+id, headers = headers)
    print(LoanProfile.content)



def loanProfile_view(request):

    return render(request, 'mainApp/loanProfile.html', getId())
