from django.views import View
from django.http import HttpResponse 
from django.shortcuts import render

class HomePage(View):
    
    def get(self,request):
        return render(request,'index.html')