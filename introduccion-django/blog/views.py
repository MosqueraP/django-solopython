from django.shortcuts import render
from django.views import View
from blog.forms import PosteCreateForm

# Create your views here.

class BlogListView(View):
    def get(self, request, *args, **kw):
        context={
        }
        return render(request, 'blog_list.html', context)

class BlogCreateView(View):
    def get(self, request, *args, **kw):
        context={
        }
        return render(request, 'blog_create.html', context)
    
    def post(self, request, *args, **kw):
        context={
        }
        return render(request, 'blog_create.html', context)