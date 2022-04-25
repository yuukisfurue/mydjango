from django.shortcuts import render
from django.http import HttpResponse
from .models import Member
from .forms import BoardForm

def index(request):
    params = {
        'title': 'Board',
        'message': 'all members.',
        'form':BoardForm(),
        'data': [],
    }
    if (request.method == 'POST'):
        num=request.POST['id']
        item = Member.objects.get(id=num)
        params['data'] = [item]
        params['form'] = BoardForm(request.POST)
    else:
        params['data'] = Member.objects.all()
    return render(request, 'Board/index.html', params)