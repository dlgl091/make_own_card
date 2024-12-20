from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name = 'index'), # 첫 번째 인자에 라우팅 문자열. 매개변수는 <int:question_id> 이런식
    path('result', views.result, name = 'result'),
    path('step2', views.step_2, name = 'step_2')
    #static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
]