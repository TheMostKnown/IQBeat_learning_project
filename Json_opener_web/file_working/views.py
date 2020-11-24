from django.shortcuts import render
from django.http import HttpResponse

from .forms import DocumentForm

import json

def handle_uploaded_file(f):
    with open('use_it.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def index(request):
    if request.method == "GET":
        return render(request, 'index.html')
    elif request.method == "POST":
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            k = request.POST['key']
            try:
                with open('use_it.txt', 'r') as text:
                    t = json.load(text)
                    if k == '*':
                        return HttpResponse(t)
                    else:
                       return HttpResponse(t[k])
            except Exception:
                return HttpResponse("Something_go_wrong")
        else: return HttpResponse("Something_go_wrong")