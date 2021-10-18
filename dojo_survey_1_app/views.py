from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def result(request):
    yr_name=request.POST['your_name']
    print(request.POST)
    loc=request.POST['location']
    fv_lang=request.POST['fav_lang']
    comm=request.POST['comment']
    context= {
        'result': request.POST
    }
    return render(request, 'result.html', context)

