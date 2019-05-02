from django.shortcuts import render, get_object_or_404
from ckeditor.widgets import CKEditorWidget
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView

from .models import Post
# Create your views here.
def index(request):
    return render(request,'blog/home.html')

class BlogListView(ListView):
    model = Post
    template_name = "blog/articles.html"
    paginate_by = 5
    context_object_name = 'posts'
    queryset = Post.objects.filter(status=True)
    ordering = ['-post_update',]

def about(request):
    template = "blog/about.html"
    return render(request,template)
class test(TemplateView):
    template_name = 'base2.html'