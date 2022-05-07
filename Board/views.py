from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Member
from .forms import MemberForm
from django.views.generic import ListView
from django.views.generic import DetailView
from django.db.models import Q 
from django.db.models import Count,Sum,Avg,Min,Max
from .forms import CheckForm
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.validators import MinLengthValidator
from django.core.validators import URLValidator  
from django.core.validators import RegexValidator 
from django.core.paginator import Paginator

class MemberList(ListView):
    model = Member

class MemberDetail(DetailView):
    model = Member

def index(request, num=1):
    data = Member.objects.all()
    page = Paginator(data, 5)
    params = {
        'title': 'Board',
        'message':'',
        'data': page.get_page(num),
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

def edit(request, num):
    obj = Member.objects.get(id=num)
    if (request.method == 'POST'):
        member = MemberForm(request.POST, instance=obj)
        member.save()
        return redirect(to='/Board')
    params = {
        'title': 'Board',
        'id':num,
        'form': MemberForm(instance=obj),
    }
    return render(request, 'Board/edit.html', params)

def delete(request, num):
    member = Member.objects.get(id=num)
    if (request.method == 'POST'):
        member.delete()
        return redirect(to='/Board')
    params = {
        'title': 'Board',
        'id':num,
        'obj': member,
    }
    return render(request, 'Board/delete.html', params)

def find(request):
    if (request.method == 'POST'):
        msg = request.POST['find']
        form = FindForm(request.POST)
        sql = 'select * from Board_member'
        if (msg != ''):
            sql += ' where ' + msg
        data = Member.objects.raw(sql)
        msg = sql
    else:
        msg = 'search words...'
        form = FindForm()
        data =Member.objects.all()
    params = {
        'title': 'Board',
        'message': msg,
        'form':form,
        'data':data,
    }
    return render(request, 'Board/find.html', params)

def check(request):
    params = {
        'title': 'Board',
        'message':'check validation.',
        'form': MemberForm(),
    }
    if (request.method == 'POST'):
        obj = Member()
        form = MemberForm(request.POST, instance=obj)
        params['form'] = form
        if (form.is_valid()):
            params['message'] = 'OK!'
        else:
            params['message'] = 'no good.'
    return render(request, 'Board/check.html', params)