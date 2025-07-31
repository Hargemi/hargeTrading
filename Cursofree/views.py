from django.shortcuts import render

# Create your views here.
def tradingfree(request):   
    return render(request, 'Cursofree/tradingfree.html')  # Asegúrate de que esta plantilla exista en templates/Cursofree/