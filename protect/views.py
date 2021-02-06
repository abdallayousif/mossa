from django.shortcuts import render
from .models import Products

# Create your views here.
def Prodect_list(request):
    Pro_lest = Products.objects.all()
    contxet = {
        'Products' :Pro_lest
    }
    return render(request,'Prodect/Prodect.html',contxet)


def Prodect_det(request):
    pass

