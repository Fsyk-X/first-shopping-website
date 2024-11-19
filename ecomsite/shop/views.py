from django.shortcuts import render
from .models import Products, Order
from django.core.paginator import Paginator
# Create your views here.

def indexView(request):
    allProducts = Products.objects.all()
    #SEARCH FUNCTIONALITY
    prod_search = request.GET.get('product_name')
    if prod_search != '' and prod_search is not None:
        allProducts = allProducts.filter(prodTitle__icontains=prod_search)

    #PAGINATOR
    myPaginator = Paginator(allProducts, 3)
    pageNumber = request.GET.get('page')
    allProducts = myPaginator.get_page(pageNumber)

    return render(request, 'shop/index.html', {'allProducts' : allProducts})

def detailView(request, id):
    productDetail = Products.objects.get(id=id)
    return render(request, 'shop/detail.html', {'productDetail' : productDetail})

def checkoutView(request):

    if request.method == "POST":
        items = request.POST.get('items','')
        name = request.POST.get('name',"")                                  #The empty strings are Default Values
        email = request.POST.get('email',"")
        address = request.POST.get('address',"")
        city = request.POST.get('city',"")
        state = request.POST.get('state',"")
        zipcode = request.POST.get('zipcode')
        total = request.POST.get('total')
        custOrder = Order(total = total,items = items,custName=name, custEmail=email, custAddress = address, custCity = city, custState = state, custZipcode = zipcode)
        custOrder.save()
    
    return render(request, 'shop/checkout.html')