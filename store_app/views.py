from django.shortcuts import render, redirect
from .models import Product
from django.http import HttpResponse
from  .forms import OrderForm

def product_list(request):
    products = Product.objects.all()
    return render(request, 'store/product_list.html', {'products': products})

def order_product(request):
    if request.method == 'POST':
    
        product_id = request.POST.get['product_id']
        size = request.POST.get['size']
        quantity = request.POST.get['quantity']
        name = request.POST.get['name']
        phone_number = request.POST.get['phone_number']

# getting the product object
        product = Product.objects.get(id=product_id)

        # message for whatsapp
        message = f"I would like to order {product.name} (Size: {size}, Quantity: {quantity}).\nName: {name}\nPhone: {phone_number}"
        # generate whatsapp link
        whatsapp_url = f"https://wa.me/254720630112?text={message}"

        # redirect to whatsapp
        return redirect(whatsapp_url)
    return render(request, 'store/order_product.html')




