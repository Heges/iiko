from decimal import Decimal

from django.contrib.sessions.models import Session

from dishes.models import Dishes


class Cart(object):

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('cart')
        if not cart:
            cart = request.session['cart'] = {}
        self.cart = cart

    def add(self, item, quantity=1, update_quantity=False):
        product_id = item.id
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': item.counts,
                                     'price': str(item.price),
                                     'name': str(item.name),
                                     'id': item.id
                                     }
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        self.session['cart'] = self.cart
        self.session.modified = True

    def __iter__(self):
        product_ids = self.cart.keys()
        filtered_product = Dishes.objects.filter(id__in=product_ids)
        for obj in filtered_product:
            self.cart[str(obj.id)]['obj'] = obj

        for item in self.cart.values():
            item['total_price'] = int(item['price']) * int(item['quantity'])
            yield item

    def get_total_price(self):
        return sum(Decimal(item['price']) * int(item['quantity']) for item in
                   self.cart.values())

    def remove(self, item):
        product_id = str(item.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.session['cart'] = self.cart
            self.session.modified = True

    def clear(self):
        Session.objects['cart'].delete()

    # def add_quantity(self, item, quantity):
    #     product_id = item.id
    #     if product_id in self.cart:
    #         self.cart[product_id]['quantity'] = quantity
    #         self.session['cart'] = self.cart
    #         self.session.modified = True


def get_quantity(self, item):
    product_id = str(item.id)
    return self.cart[product_id]['quantity']
