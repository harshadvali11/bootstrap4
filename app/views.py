from django.shortcuts import render

# Create your views here.

def cdnmethod(request):
    return render(request,'cdnmethod.html')


def downloadmethod(request):
    return render(request,'downloadmethod.html')