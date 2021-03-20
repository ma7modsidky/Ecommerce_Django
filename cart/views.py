from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Product
from .cart import Cart
from .forms import CartAddProductForm
from coupons.forms import CouponApplyForm

from django.http import JsonResponse, HttpResponse
import json
# Create your views here.

@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                quantity=cd['quantity'],
                override_quantity=cd['override'])
    return redirect('cart:cart_detail')


@require_POST
def cart_add_ajax(request):
    cart = Cart(request)
    data = json.loads(request.body)
    product_id = data['product_id']
    if product_id :
        if cart.in_cart(product_id) :
            return JsonResponse({'status': 'already'})
        else :
            try :
                product = get_object_or_404(Product, id=product_id)
                cart.add(product = product,
                        quantity = 1,
                        override_quantity = True)      
                return JsonResponse({'status': 'ok'})
            except : 
                return JsonResponse({'status': 'no'})
    return JsonResponse({'status': 'error'})


@require_POST
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={
            'quantity': item['quantity'],
            'override': True})
    coupon_apply_form = CouponApplyForm()
    return render(request, 'cart/detail.html', {'cart': cart ,
                                                'coupon_apply_form': coupon_apply_form})

