from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def result(request):
    yr_name=request.POST['your_name']
    loc=request.POST['location']
    fv_lang=request.POST['fav_lang']
    context= {
        'result': request.POST
    }
    return render(result, 'result.html', context)

