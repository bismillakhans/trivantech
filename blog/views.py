from django.shortcuts import render, get_object_or_404
from ckeditor.widgets import CKEditorWidget
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView

from .models import Post,Student,Document,Member,Link,Work,Gallery
# Create your views here.
def index(request):
    return render(request,'blog/home.html')

class BlogListView(ListView):
    model = Post
    template_name = "blog/articles.html"
    paginate_by = 10
    context_object_name = 'posts'
    queryset = Post.objects.filter(status=True)
    ordering = ['-post_update',]


class MemberListView(ListView):
    model = Member
    template_name = "blog/members.html"
    context_object_name = 'members'
    queryset = Member.objects.filter(status=True)
    ordering = ['rank',]

class DocumentListView(ListView):
    model = Document
    template_name = "blog/document.html"
    context_object_name = 'docs'
    queryset = Document.objects.filter(status=True)

class GalleryListView(ListView):
    model = Gallery
    template_name = "blog/gallery.html"
    context_object_name = 'galleries'
    queryset = Gallery.objects.filter(status=True)
    ordering = ['-g_date',]

def about(request):
    template = "blog/about.html"
    return render(request,template)
class test(TemplateView):
    template_name = 'base2.html'

def post_view(request, year, month, slug):
    template = 'blog/post.html'
    post = get_object_or_404(Post, post_date__year=year,
                             post_date__month=month, slug=slug)
    context = {'post': post}
    return render(request,'blog/post.html',context)

class RegisterStudent(CreateView):
    model = Student
    fields = ['name', 'district', 'phone','email', 'organisation', 'address']
    success_url = '/reg_success'

class RegSuccess(TemplateView):
    template_name = "blog/reg_success.html"