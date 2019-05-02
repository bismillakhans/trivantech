
from django.urls import path
from  . import views

# from django.conf import settings
# from django.conf.urls.static import static

app_name='blog'

urlpatterns = [


path('', views.index, name='home'),
path('articles/', views.BlogListView.as_view(), name='articles'),
path('test/', views.test.as_view(), name='test'),
path('<int:year>/<int:month>/<slug:slug>', views.post_view, name='post'),
path('about/', views.about, name='about'),

]
