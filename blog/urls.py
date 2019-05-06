
from django.urls import path
from  . import views

# from django.conf import settings
# from django.conf.urls.static import static

app_name='blog'

urlpatterns = [


path('', views.index, name='home'),
path('articles/', views.BlogListView.as_view(), name='articles'),
path('student/', views.RegisterStudent.as_view(), name='student'),
path('gallery/', views.GalleryListView.as_view(), name='gallery'),
path('documents/', views.DocumentListView.as_view(), name='documents'),
path('members/', views.MemberListView.as_view(), name='members'),
path('works/',views.WorkListView.as_view(),name="works"),
path('search/', views.post_search, name='search'),

path('<int:year>/<int:month>/<slug:slug>', views.post_view, name='post'),
path('about/', views.about, name='about'),
path('reg_success/', views.RegSuccess.as_view(), name='reg_successview'),

]

