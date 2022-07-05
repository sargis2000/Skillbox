from decimal import Decimal
from django.conf import settings



class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, magazine, quantity=1, update_quantity=False):
        product_id = str(product.id)
        magazine_id = str(magazine.id)
        magazine_dict = {
                    'product_id': product.id,
                    'product_name': product.name,
                    'magazine_id': magazine.id,
                    'magazine_name': magazine.name,
                    'quantity': 0,
                    'price': str(product.price)}

        if product_id not in self.cart:
            self.cart[product_id] = {
                magazine_id: magazine_dict}

        else:
            if magazine_id not in self.cart[product_id]:
                self.cart[product_id][magazine_id] = magazine_dict

        if update_quantity:
            self.cart[product_id][magazine_id]['quantity'] = quantity
        else:
            self.cart[product_id][magazine_id]['quantity'] += quantity
        self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self, product, market):
        product_id = str(product.id)
        market_id = str(market.id)
        if product_id in self.cart:
            if market_id in self.cart[product_id]:
                del self.cart[product_id][market_id]
                self.save()

    def __iter__(self):
        for item in self.cart.values():
            for magazine in item.values():
                magazine['price'] = Decimal(magazine['price'])
                magazine['total_price'] = magazine['price'] * magazine['quantity']
                yield magazine

    def __getitem__(self, product_id):
        return self.cart[product_id]

    def __len__(self):
        return sum(magazine['quantity'] for item in self.cart.values() for magazine in item.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in
                   self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
