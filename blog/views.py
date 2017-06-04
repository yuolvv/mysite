from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from blog.models import Blog

# Create your views here.
def hello(request):
    return HttpResponse('<html>Hello Django</html>')

def showBlog(request,blogId):
    t = loader.get_template('blog.html')
    blog = Blog.objects.get(id=blogId)
    context = {'blog':blog}
    html = t.render(context)
    return HttpResponse(html)

def showBlog_list(request):
    t = loader.get_template('blog_list.html')
    blogs = Blog.objects.all()
    context = {'blogs':blogs}
    html = t.render(context)
    return HttpResponse(html)