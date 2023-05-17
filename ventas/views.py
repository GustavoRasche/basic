from django.shortcuts import render

# Create your views here.
def ventalist(request):
    return render(request, 'ventaslist.html')
