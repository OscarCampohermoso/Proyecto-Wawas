from django.shortcuts import render

def service(request):
    return render(request, 'service.html')
