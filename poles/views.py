from django.shortcuts import render

def immobilier(request):
    return render(request, 'poles/immobilier.html')

def invest(request):
    return render(request, 'poles/invest.html')
def international(request):
    return render(request, 'poles/international.html')

def mobility(request):
    return render(request, 'poles/mobility.html')
def solutions(request):
    return render(request, 'poles/solutions.html')  
