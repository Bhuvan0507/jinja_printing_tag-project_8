from django.shortcuts import render

# Create your views here.

def data_render(request):
    data='The data is our assumption'
    D={'assumption':data}


    return render(request,'data_render.html',context=D)
