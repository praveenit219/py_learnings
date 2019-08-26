from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ProductForm, RawProductForm
from .models import Product

"""
def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()
    context = {
        'form': form
    }
    return render(request, "products/product_create.html", context)
"""

"""
def product_create_view(request):
    my_title = request.POST.get('title')
    print(my_title)
    context = {}
    return render(request, "products/product_create.html", context)
"""
"""
def product_create_view(request):
    myForm = RawProductForm()
    if request.method == 'POST':
        myForm = RawProductForm(request.POST)
        if myForm.is_valid():
            print(myForm.cleaned_data)
            Product.objects.create(**myForm.cleaned_data)
        else:
            print(myForm.errors)
    context = {
        'form': myForm
    }
    return render(request, "products/product_create.html", context)
"""


def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()
    context = {
        'form': form
    }
    return render(request, "products/product_create.html", context)


#set initial data in form
def render_initial_data(request):
    initialData = {
        'title': "My initial title"
    } 
    obj = Product.objects.get(id=1)
    #myForm = RawProductForm(request.POST or None, initial=initialData)    
    myForm = ProductForm(request.POST or None, initial=initialData, instance=obj)
    if myForm.is_valid():
        myForm.save()
    else:
        print('not a valid form')
    context = {
        'form': myForm
    }
    return render(request, "products/product_create.html", context)

    
def product_detail_view(request):
    obj = Product.objects.get(id=1)
    """ context = {
        'title' : obj.title,
        'description': obj.description,
        'price': obj.price,
        'summary': obj.summary,
        'isFeatured': obj.featured
    } """

    context = {
        'object': obj
    }
    return render(request,'products/product_detail.html',context)

def dynamic_lookup_view(request,id):
    #obj = Product.objects.get(id=id)
    #obj = get_object_or_404(Product, id=id) #if we need to show 404 when object not found from db

    #if you need Http 404 instead of getobject we can use try raise
    try:
        obj = Product.objects.get(id=id)
    except Product.DoesNotExist:
        raise Http404        
    context = {
        'object': obj
    }
    return render(request, 'products/product_detail.html', context)


def product_delete_view(request, id):
    obj = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        obj.delete()
        return redirect('../') # give correct url where you want to go after deletions
    context = {
        'object': obj
    }
    return render(request, 'products/product_delete.html', context)


def product_list_view(request):
    queryset = Product.objects.all() #all list of objects
    context = {
        'object_list': queryset        
    }
    return render(request,'products/product_list.html',context)