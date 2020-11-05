# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from requests.auth import HTTPBasicAuth
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
#from import_export export loanProfile_view

import requests
import json
import pprint


# Create views here.
def home_view(request):
    if request.method == 'POST':
        url = 'https://films.dalexapps.com/FilmsWeb/api/web/loginuser'
        username = request.POST.get('Username')
        password = request.POST.get('Password')
        if username == '56-0001-00018' and password == '9999':
            headers = {'Content-Type': 'application/json'}
            LogUser = requests.post(url+'?username='+username+'&'+'password='+password, headers = headers)
            return redirect('loanprofile')
        else:
            print('Not correct')
    return render(request, 'mainApp/weblinq.html')






def loanProfile_view(request):
    body = 'No response yet, Enter Loan ID'
    url = 'https://films.dalexapps.com/FilmsWeb/api/web/getloanrequest'
    id = request.POST.get('LoanID')
    if id is not None:
        headers = {'Content-Type': 'application/json'}
        LoanProfile = requests.get(url+'?id='+id, headers = headers)
        body = json.loads(LoanProfile.content)
        pprint.pprint(body)
    return render(request, 'mainApp/loanProfile.html', {'response': body})
