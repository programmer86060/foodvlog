from . models import *
from .views import *

def count(request):
    item_count = 0
    if 'admin' in request.path:                                                                                           #correct etra count undenn nokaanum pinne items delete cheyyaanumoke aan ith
        return {}
    else:
        try:
            ct = cartlist.objects.filter(cart_id=c_id(request))
            cti = cart_items.objects.all().filter(cart=ct[:1])
            for c in cti:
                item_count+=c.quatity
        except cartlist.DoesNotExist:
            item_count = 0
        return dict(itc=item_count)