from django.shortcuts import render, get_object_or_404
from category.models import Category
from .models import Product
from carts.models import CartItem
from carts.views import _cart_id
from django.db.models import Q
from django.core.paginator import EmptyPage, Paginator, PageNotAnInteger

from django.shortcuts import render, get_object_or_404
from category.models import Category
from .models import Product
from carts.models import CartItem
from carts.views import _cart_id
from django.core.paginator import EmptyPage, Paginator, PageNotAnInteger

from django.http import HttpResponse
def store(request, category_slug=None):
    category = None

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        # Add order_by here for consistent pagination
        products = Product.objects.filter(category=category, is_available=True).order_by('id')
        paginator = Paginator(products, 1)  # 1 per page for testing
    else:
        products = Product.objects.filter(is_available=True).order_by('id')
        paginator = Paginator(products, 3)  # 3 per page for main store

    page = request.GET.get('page')
    paged_products = paginator.get_page(page)
    product_count = products.count()

    context = {
        'products': paged_products,
        'product_count': product_count,
    }

    return render(request, 'store/store.html', context)

def product_detail(request, category_slug, product_slug):
    try:
        single_product = Product.objects.get(category__slug=category_slug,slug=product_slug)
        in_cart=  CartItem.objects.filter(cart__cart_id=_cart_id(request), product=single_product).exists()
          
    except Exception as e: 
     raise e
    context = {
        'single_product': single_product,
        'in_cart'       : in_cart,

}
    return render(request,'store/product_detail.html',context)


def search(request):
    products = Product.objects.none()   # 🔴 default = no products
    product_count = 0

    keyword = request.GET.get('keyword')

    if keyword:
        keyword = keyword.strip()

        if keyword != "":
            products = Product.objects.filter(
                Q(description__icontains=keyword) |
                Q(product_name__icontains=keyword)
            ).order_by('-created_at')

            product_count = products.count()

    context = {
        'products': products,
        'product_count': product_count,
    }

    return render(request, 'store/store.html', context)