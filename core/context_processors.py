from .models import *


def categ(request):
    # if request.user.is_authenticated:
    #     request.session.set_expiry(100)
    #     return {'categories':Category.objects.all(),'owner':request.user,'expiry':request.session['_session_expiry']*1000}
    # else:
    #     return {'categories':Category.objects.all()}
    return {}