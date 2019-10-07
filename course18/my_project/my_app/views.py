from django.shortcuts import render
from django.template import RequestContext
from django.views.generic import View
from django.contrib import messages

from my_app.forms import MyForm


def index(request):
    if request.method == 'GET':
        return render(request,
                      'my_app/index.html',
                      {'name': 'Pavel',
                       'another': 'I'})






class MyView(View):

    def get(self, request):
        form = MyForm()
        c = {'form': form}
        return render(request,
                      'my_app/form.html',
                      c)

    def post(self, request):
        form = MyForm(data=request.POST)
        if form.is_valid():
            messages.success(request,
                             form.cleaned_data['message'])
        else:
            messages.error(request, 'Validation failed')

        c = {'form': form}
        #c = {'form': MyForm()}

        return render(request, 'my_app/form.html', c)
