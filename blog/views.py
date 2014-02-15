from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext,loader
from blog.models import Blog
from blog.models import Posting

# Create your views here.

def blog(request):
  template=loader.get_template('blog/index.html')
  if request.method=='POST':
    form=Blog(request.POST)
    if form.is_valid():
      text=form.cleaned_data['text']
      header=form.cleaned_data['header']
      user=Posting(writing=text,user=header)
      user.save()
      return HttpResponse('<html><head></head><body>Success</body></html>')
  else:
    form = Blog()
    context=RequestContext(request,{'x':form,},)
    return HttpResponse(template.render(context))
