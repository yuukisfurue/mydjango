from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.generic import ListView
from django.views.generic import DetailView
from .forms import FindForm 
from django.core.paginator import Paginator
from django.db.models import Q    # 追記
from django.db.models import Count,Sum,Avg,Min,Max
from .forms import CheckForm    #☆
from django.core.paginator import Paginator
from .forms import MemberForm
from .models import Member
import csv

class MemberList(ListView):
    model = Member

class MemberDetail(DetailView):
    model = Member

def index(request, num=1):
    data = Member.objects.all()
    page = Paginator(data, 10)
    params = {
        'title': 'Board',
        'message':'',
        'data': page.get_page(num),
    }
    return render(request, 'board/index.html', params)

# create model
def create(request):
    if (request.method == 'POST'):
        obj = Member()
        member = MemberForm(request.POST, instance=obj)
        member.save()
        return redirect(to='/board')
    params = {
        'title': 'Board',
        'form': MemberForm(),
    }
    return render(request, 'board/create.html', params)

def edit(request, num):
    obj = Member.objects.get(id=num)
    if (request.method == 'POST'):
        member = MemberForm(request.POST, instance=obj)
        member.save()
        return redirect(to='/board')
    params = {
        'title': 'Board',
        'id':num,
        'form': MemberForm(instance=obj),
    }
    return render(request, 'board/edit.html', params)

def delete(request, num):
    member = Member.objects.get(id=num)
    if (request.method == 'POST'):
        member.delete()
        return redirect(to='/board')
    params = {
        'title': 'Board',
        'id':num,
        'obj': member,
    }
    return render(request, 'board/delete.html', params)

def find(request):
    if (request.method == 'POST'):
        msg = request.POST['find']
        form = FindForm(request.POST)
        sql = 'select * from board_member'
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
    return render(request, 'board/find.html', params)

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
    return render(request, 'board/check.html', params)

def csv_export(request):
	filename='export.csv'
	response = HttpResponse(content_type='text/csv;charset=utf_8_sig')
	response['Content-Disposition'] = "attachment;  filename='{}'; filename*=UTF-8''{}".format(filename, filename)

	w = csv.writer(response)
	w.writerow(['id','name','prefecture','gender','employmentstatus','company','jyob','stay','affiliation','potion','annual','lastyear'])
	    
	data = Member.objects.all()
	for item in data:
		w.writerow([item.id, item.name, item.prefecture, item.gender, item.employmentstatus,item.company, item.jyob, item.stay, item.affiliation, item.postion, item.annual, item.lastyear])
	return response


