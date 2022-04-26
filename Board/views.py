from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Member
from .forms import MemberForm

def index(request):
    data = Member.objects.all()
    params = {
        'title': 'Board',
        'data': data,
    }
    return render(request, 'Board/index.html', params)

# create model
def create(request):
    if (request.method == 'POST'):
        obj = Member()
        member = MemberForm(request.POST, instance=obj)
        member.save()
        return redirect(to='/Board')
    params = {
        'title': 'Board',
        'form': MemberForm(),
    }
    return render(request, 'Board/create.html', params)
