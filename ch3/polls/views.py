from django.shortcuts import get_object_or_404, render, redirect
from django.http import JsonResponse, Http404
from django.core.files.storage import default_storage
from .models import GeneratedCard, TemplateCard
import json


# Create your views here.
def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'polls/index.html')


def result(request):
    return render(request, 'polls/result.html')
def step_1(request):
    return render(request, 'polls/step_1.html')
def step_2(request):
    if request.method == 'GET':
        card_ls = ['health', 'love', 'luck', 'money', 'mycat', 'mydog', 'pass', 'switchJob']
        id = request.GET.get('mode')
        if id:
            if id in card_ls:
                id1 = id + "_1_img.png"
                id2 = id + "_2_img.png"
                data = {
                    'img1': id1,
                    'img2': id2,
                }
                return render(request, 'polls/step_2.html', data)
            else :
                # 'mode' 파라미터 잘못된 경우
                raise Http404('잘못된 요청입니다.')
        else:
                # 'mode' 파라미터가 없으면 메인 페이지로 리다이렉트
                return redirect('polls:index')  # URL 패턴 이름 사용
    else:
        # GET 요청이 아닌 경우에도 메인 페이지로 리다이렉트
        return redirect('polls:index')

def test(request):
    return render(request, 'polls/test.html')

def upload_image(request):
    if request.method == 'POST' and request.FILES['image']:
        image = request.FILES['image']
        file_path = default_storage.save(f'upload/{image.name}', image)
        return JsonResponse({'message': 'Image uploaded successfully', 'file_path': file_path})
    return JsonResponse({'error': 'Invalid request'}, status=400)

def save_data(request):
    if request.method == 'POST':
        try:
            mode_dict = {
                'luck':1,
                'love':2,
                'switchJob':3,
                'pass':4,
                'money':5,
                'health':6,
                'myCat':7,
                'myDog':8
            }
            
            image = request.FILES.get('image')
 
            file_path = default_storage.save(f'upload/{image.name}', image)
        
            data1 = request.POST.get('text1')
            data2 = request.POST.get('text2')
            mode = request.POST.get('mode')
            
            # db에 저장
            # template_card_instance = TemplateCard.objects.get(id=mode_dict[mode])
            GeneratedCard.objects.create(cardNo_id=mode_dict[mode], cardName=mode, genImgLink=file_path, text1=data1, text2=data2)
            return JsonResponse({'status': 'success'})

        
            #return JsonResponse({'message': 'Image uploaded successfully', 'file_path': file_path, 'text1':data1, 'text2':data2, 'mode':mode})
        except Exception as e:
            return JsonResponse({'status': e})
 

    return JsonResponse({'status': 'failed'}, status=400)