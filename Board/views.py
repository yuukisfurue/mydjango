from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import BoardForm

class BoardView(TemplateView):
    
    def __init__(self):
        self.params = {
            'title': 'Board',
            'form': BoardForm(),
            'result':None
        }
    
    def get(self, request):
        return render(request, 'Board/index.html', self.params)

    def post(self, request):
        ch = request.POST.getlist('choice')
        self.params['result'] = 'selected: ' + str(ch) + '.'
        self.params['form'] = BoardForm(request.POST)
        return render(request, 'Board/index.html', self.params)