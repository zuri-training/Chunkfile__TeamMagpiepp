from django.shortcuts import render
from datetime import datetime
import os
from urllib import response
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.template import loader
from os import listdir
import pandas as pd
from os.path import isfile, join
from django.views.generic.base import TemplateView
from pathlib import Path
# import mimetypes
from django.http import FileResponse


# Create your views here.
def dashboard(request):
    return render(request, "")

def fileAuthen(request):
    documents = Documents.objects.filter(user=request.user)
    print(documents)
    return render(request, '', {'files': documents})

def myfile(request):
    documents = Documents.objects.filter(user=request.user)
    print(documents)
    return render(request, '', {'files'}: documents)

def delete(request):
    filename = request.GET.get('filename')
    documents = Documents.objects.filter(user=request.user,docfile=filename)
    documents.delete()
    return redirect('prototype:myfile')

# def chunkfile(request):
#     if request.method == 'POST':
#         file_setting = request.FILES['selectedfile']
#         file_setting_name = file_setting.name
#         file_ext = file_setting.name.split