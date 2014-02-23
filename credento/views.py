from django.shortcuts import render
from django.template import loader,RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib import auth
from django.core.context_processors import csrf
from credento.models import Register,user_model

def login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('login.html',c)

def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username = username, password = password)

    if user is not None:
        auth.login(request,user)
        return HttpResponseRedirect('/accounts/loggedin')
    else:
        return HttpResponseRedirect('/accounts/invalid')

def loggedin(request):
    return render_to_response('loggedin.html',
                              {'full_name':request.user.username})

def invalid_login(request):
    return render_to_response('invalid_login.html')

def logout(request):
    auth.logout(request)
    return render_to_response('logout.html')
                              
def register_user(request):
    template=loader.get_template('credento/usereg.html')
    if request.method=='POST':
        form=Register(request.POST)
        if form.is_valid():
            firstname=form.cleaned_data['firstname']
            lastname=form.cleaned_data['lastname']
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            phone=form.cleaned_data['phone']
            u=user_model(firstname=firstname,laststname=lastname,username=username,password=password,phone=phone)
            u.save()
            return HttpResponse('<html><head></head><body>Successfully registered</body></html>')
    else:
        form = Register()
        context=RequestContext(request,{'x':form,},)
        return HttpResponse(template.render(context))


def register_true(request):
    return render_to_response('register_true.html')

# Create your views here.
