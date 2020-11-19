from django.shortcuts import render
from django.http import HttpResponse

from .forms import DocumentForm

import json

def index(request):
    if request.method == "GET":
        return render(request, 'index.html')
    elif request.method == "POST":
        form = DocumentForm(request.POST)
        if form.is_valid():
            text = json.load(form['file'])
            k = form['key']
            return HttpResponse(text[k])