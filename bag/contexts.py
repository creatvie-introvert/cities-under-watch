from decimal import Decimal
from products.models import Product


def bag_contents(request):
    bag_items = []
    total = Decimal('0.00')
    product_count = 0

    bag = request.session.get('bag', {})

    for item_id in bag.keys():
        product = Product.objects.get(id=item_id)
        total += product.price
        product_count += 1

        bag_items.append({
            'item_id': item_id,
            'product': product,
        })

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
    }

    return context
