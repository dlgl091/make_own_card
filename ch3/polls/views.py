from django.shortcuts import get_object_or_404, render


# Create your views here.
def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'polls/index.html')

def result(request):
    return render(request, 'polls/result.html')

def step_2(request):
    return render(request, 'polls/step_2.html')