from django.shortcuts import render

# Create your views here.
def cond(request):
    d={'a':300,'b':400,'c':500}
    return render(request,'cond.html',d)