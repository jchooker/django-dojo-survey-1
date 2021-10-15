from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def result(request):
    context= {
        'result': request.POST
    }
    return render(result, 'result.html', context)

