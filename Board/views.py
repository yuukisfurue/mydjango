from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Member
from .forms import BoardForm

def index(request):
    data = Member.objects.all()
    params = {
        'title': 'Board',
        'data': data,
    }
    return render(request, 'Board/index.html', params)

# create model
def create(request):
    params = {
        'title': 'Board',
        'form': BoardForm(),
    }
    if (request.method == 'POST'):
        name = request.POST['name']
        age = request.POST['age']
        gender = 'gender' in request.POST
        pref = int(request.POST['pref'])
        jyob = request.POST['jyob']
        pojishon = request.POST['pojishon']
        member.save()
        return redirect(to='/Board')
    return render(request, 'Board/create.html', params)