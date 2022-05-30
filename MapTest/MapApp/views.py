from django.shortcuts import render, redirect
from .models import Concert
from django.utils import timezone

# Create your views here.

def home(request):
    return render(request, 'no_account.html')


def concert_form(request):
    return render(request, 'concert_form.html')

def create(request):
    if(request.method == 'POST'):
        concert = Concert() 
        concert.introduce = request.POST['introduce'] 
        concert.date = request.POST['date']
        concert.time = request.POST['time']
        concert.latitude = request.POST['latitude']
        concert.logitude = request.POST['longitude']
        concert.save() # 모델객체이름.save()를 통해 모델객체를 데이터베이스에 저장
    return redirect('home') # 정상적으로 끝났으면 home으로 돌아간다 (앞서 redirect를 import 해줘야함)