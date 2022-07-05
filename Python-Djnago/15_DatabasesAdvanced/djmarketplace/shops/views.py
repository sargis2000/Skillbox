from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from django.views.decorators.http import require_POST, require_GET
from app_users.models import Profile
from cart.cart import Cart
from cart.forms import CartAddProductForm
from .models import Product, MarketModel
from django.views.generic import ListView


class ProductListView(ListView):
    template_name = 'shop.html'
    context_object_name = 'products'
    queryset = Product.objects.prefetch_related('market').all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CartAddProductForm()
        return context


@login_required(login_url='/accounts/login/')
@require_POST
def buy(request):
    product_id = request.POST['product_id']
    magazine_id = request.POST['magazine_id']
    cart = Cart(request)
    cart_values = cart[product_id][magazine_id]
    profile = Profile.objects.get(user=request.user)
    product = get_object_or_404(Product, id=int(product_id))
    market = get_object_or_404(MarketModel, id=int(magazine_id))
    product.count -= cart_values['quantity']
    product.sold += cart_values['quantity']
    product.save()
    profile.balance -= cart_values['quantity'] * int(cart_values['price'])
    profile.save()
    cart.remove(product, market)
    return redirect('cart_detail')

@require_GET
def popularitems(request):
    return render(request, 'popularitems.html', {'products': Product.objects.all().order_by('sold')})

