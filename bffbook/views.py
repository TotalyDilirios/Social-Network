from django.http import HttpResponse
from django.shortcuts import render
from django.utils.translation import gettext as _

def home_view(request):
    user = request.user
    hello = _('Hello world')

    context = {
        'user': user,
        'hello' : hello,
    }
    return render(request, 'main/home.html', context)
    # return HttpResponse('Hello world')