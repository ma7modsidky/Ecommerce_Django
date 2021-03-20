from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm
from django.views.decorators.csrf import ensure_csrf_cookie
from .forms import SearchForm, ContactForm
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
# Create your views here.

def home(request):
    products = Product.objects.filter(available=True)[:5]
    return render(request, 'shop/home.html', {'products': products})


class about_us(TemplateView):
    template_name = "shop/about_us.html"


class contact_us(FormView):
    template_name = 'shop/contact_us.html'
    form_class = ContactForm
    success_url = 'shop/'

@ensure_csrf_cookie
def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        language = request.LANGUAGE_CODE
        category = get_object_or_404(Category,
                                     translations__language_code=language,
                                     translations__slug=category_slug)

        products = products.filter(category=category)
    return render(request,'shop/product/list.html',

                            {'category': category,
                            'categories': categories,
                            'products': products,
                             })


@ensure_csrf_cookie
def product_search(request):
    category = None
    categories = Category.objects.all()
    form = SearchForm()
    query = None
    results = []
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            products = Product.objects.filter(
                translations__name__contains=query)
            
    return render(request, 'shop/product/list.html',
                  {
                    'category': category,
                   'categories': categories,
                   'products': products,
                   'search_form': SearchForm})

def product_detail(request, id, slug):
    language = request.LANGUAGE_CODE
    product = get_object_or_404(Product,
                                id=id,
                                translations__language_code=language,
                                translations__slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    return render(request,'shop/product/detail.html', {'product': product ,
                                                       'cart_product_form': cart_product_form})
    
