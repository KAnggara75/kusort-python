from django.shortcuts import render

# Create your views here.
def index(request):
  title = "Bubble Sorting Algorithm"
  data = {
    'title' : title,
  }
  return render(request, "bubble/index.html", data)
  