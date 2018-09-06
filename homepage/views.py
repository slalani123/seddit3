from django.shortcuts import render

def home(request):
    return render(request, 'seddit3/homepage/index.html')

# Create your views here.
