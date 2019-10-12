from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

def home(request):
    return render(request,'home.html',context={'name':'bandham'})

@csrf_exempt
def add(request):
    val1 = request.POST['num1']
    val2 = request.POST['num2']
    sum_numbers = int(val1)+int(val2)
    return render(request, 'result.html', context={'result':sum_numbers})