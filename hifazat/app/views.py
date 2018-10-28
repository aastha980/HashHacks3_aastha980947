from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def index(request):
    return render(request,'app/base.html')

@csrf_exempt
def route(request):
    if request.is_ajax():
        result = request.POST.get("data")
        x = result.split()
        distance=x[0]
        distance=float(distance)
        if(distance>10):
            print("Bus derouted")
    return render(request,'app/route.html')
