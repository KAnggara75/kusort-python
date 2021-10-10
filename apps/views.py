from django.shortcuts import render
from django.http import HttpResponse

def index(request):
  title = "Visualize Sorting Algorithm with Python based Web"
  data = {
    'title' : title,
  }
  return render(request, "index.html", data)