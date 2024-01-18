from django.shortcuts import render
from django.views import View

# Create your views here.

class BlogListView(View):
    def get(self, request, *args, **kw):
        context={

        }
        return render(request, 'blog_list.html', context)
