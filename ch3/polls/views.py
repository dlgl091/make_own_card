from django.shortcuts import get_object_or_404, render


# Create your views here.
def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'polls/index.html')

def select_type(request):
    # select_mode = request.GET.get('select_mode')
    if request.method == 'GET':
        id = request.GET['select_mode']
        data = {
            'data': id,
        }
        return render(request, 'polls/step_2.html', data)

def result(request):
    return render(request, 'polls/result.html')
def step_1(request):
    return render(request, 'polls/step_1.html')
def step_2(request):
    return render(request, 'polls/step_2.html')