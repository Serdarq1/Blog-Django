from django.shortcuts import render
from .models import Post
from django.views import generic

# Create your views here.

class PostList(generic.ListView):
    queryset = Post.objects.filter(status = 1).order_by('-created_on')
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        first_post = Post.objects.filter(status=1).order_by('created_on').first()
        context['first_post'] = first_post
        return context

class DetailView(generic.DetailView):
    model = Post
    template_name = 'post_list.html'


class BlogSearchView(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Post.objects.filter(title__icontains=query).order_by('-created_on')
