from django.shortcuts import render

def index(request):
  data = {
    'title' : "Home Page",
    'subtitle' : "Home Page | Visualize Sorting Algorithm with Python based Web",
  }
  return render(request, "sorting/index.html", data)
