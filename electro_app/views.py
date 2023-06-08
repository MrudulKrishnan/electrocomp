# from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ModeForm
from . models import SHOP

# Create your views here.


def fun1(request):
    product = SHOP.objects.all()
    return render(request, "home.html", {'products': product})


def detail(request, electro_id):
    product1 = SHOP.objects.get(id=electro_id)
    return render(request, "details.html", {'product_key': product1})


def add_comp(request):
    if request.method == 'POST':
        c_name = request.POST.get('name')
        c_desc = request.POST.get('desc')
        c_price = request.POST.get('price')
        c_img = request.FILES['img']
        c_s = SHOP(name=c_name, desc=c_desc, price=c_price, image=c_img)
        c_s.save()
        print("component added")
        return redirect('/')
    return render(request, 'add_comp.html')


def update(request, electro_id):
    obj = SHOP.objects.get(id=electro_id)
    form = ModeForm(request.POST or None, request.FILES, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit_comp.html', {'form': form, 'object': obj})


def delete(request, electro_id):
    if request.method == 'POST':
        obj = SHOP.objects.get(id=electro_id)
        obj.delete()
        return redirect('/')
    return render(request, 'delete.html')
