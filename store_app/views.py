from django.shortcuts import render, redirect
from .models import Product
from django.http import HttpResponse
from  .forms import OrderForm

def product_list(request):
    products = Product.objects.all()
    return render(request, 'store/product_list.html', {'products': products})

def order_product(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            # we extract the data from the form
            product_id = form.cleaned_data['product_id']
            quantity = form.cleaned_data['quantity']
            name = form.cleaned_data['name']
            phone_number = form.cleaned_data['phone_number']
            size = form.cleaned_data['size']

            # get the product obejct
            product = Product.objects.get(id=product_id)


            # we send whatsapp message
            order_message = f"I want to order {product.name} (Size:{size}, Quantity: {quantity}). \nName: {name}, Phone: {phone_number}"
            whatsapp_url = f"https://wa.me/254720630112text={order_message}"

            # redirect to whatsapp
            return redirect (whatsapp_url)
    else:
        form = OrderForm()


    return render(request, 'store/order_product.html', {'form': form})



