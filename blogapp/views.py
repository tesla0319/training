from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import BlogPost

class IndexView(ListView):
    template_name = 'index.html'
    context_object_name = 'orderby_records'
    queryset = BlogPost.objects.order_by('-posted_at')
    paginate_by = 4

class BlogDetail(DetailView):
    template_name='post.html'
    model = BlogPost