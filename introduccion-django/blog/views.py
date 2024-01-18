from django.shortcuts import get_object_or_404, render, redirect
from django.views import View
from blog.forms import PosteCreateForm
from blog.models import Post

# Create your views here.

class BlogListView(View):
    def get(self, request, *args, **kw):
        _posts = Post.objects.all()
        context={
            'posts': _posts 
        }
        return render(request, 'blog_list.html', context)

class BlogCreateView(View):
    # obtener informacion
    def get(self, request, *args, **kw):
        form = PosteCreateForm
        context={
            'form': form
        }
        return render(request, 'blog_create.html', context)
    
    # enviar informacion
    def post(self, request, *args, **kw):
        if request.method == 'POST':
            form = PosteCreateForm(request.POST)
            if form.is_valid():
                _title = form.cleaned_data.get('title')
                _content = form.cleaned_data.get('content')
                p, created = Post.objects.get_or_create(title=_title, content=_content)
                p.save()
                return redirect('blog:home')
            
        context={
        }
        return render(request, 'blog_create.html', context)
    


class BlogDetailView(View):
    def get(self, request, pk, *args, **kw):    
        _post = get_object_or_404(Post, pk=pk)    
        context={
            'post': _post
        }
        return render(request, 'blog_detail.html', context)
        