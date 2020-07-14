from dishes.models import Dishes


class Cart(object):

    def __init__(self, request):

        self.session = request.session
        cart = self.session.get('cart')
        if not cart:
            cart = request.session['cart'] = {}
        self.cart = cart

    def add(self, item):
        product_id = item.id
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 1,
                                     'price': str(item.price),
                                     'name': str(item.name)}
        self.session['cart'] = self.cart
        self.session.modified = True

    def __iter__(self):
        product_ids = self.cart.keys()
        filtered_product = Dishes.objects.filter(id__in=product_ids)
        for obj in filtered_product:
            self.cart[str(obj.id)]['obj'] = obj

        for item in self.cart.values():
            yield item

