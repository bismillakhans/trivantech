from django.contrib import admin
from ckeditor.widgets import CKEditorWidget
from django import forms
import csv
from .models import Post, Student, districts, Member, Document, Link, Work, Gallery
from django.http import HttpResponse


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    fields = ('title', 'tags', 'short_desc', 'body', 'img', 'status')
    list_display = ('title', 'post_date', 'status')
    list_filter = ('post_date', 'status',)
    search_fields = ('title', 'body', 'short_desc')
    date_hierarchy = 'post_date'


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    fields = ('fname', 'file', 'status', 'category')
    list_display = ('fname', 'category', 'file', 'status')
    list_filter = ('status',)


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    fields = ('linkname', 'name', 'status')
    list_display = ('linkname', 'name', 'status')
    list_filter = ('status',)


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    fields = ('title', 'img', 'status')
    list_display = ('title', 'img', 'status')
    list_filter = ('status',)


@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    fields = ('title', 'venue', 'status', 'district', 'sdate', 'info', 'wtype', 'fdate')
    list_display = ('title', 'wtype', 'venue', 'status')
    list_filter = ('status',)


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    actions = ['download_csv']
    fields = (
    'name', 'rank', 'address', 'phone', 'district', 'position', 'status', 'email', 'department', 'invigilation',
    'organisation')
    list_display = ('rank', 'name', 'address', 'phone', 'position', 'status')
    list_filter = ('rank', 'joined', 'status', 'position')
    search_fields = ('name', 'phone', 'email')

    def download_csv(self, request, queryset):
        options = districts
        mapper = {}
        for i in districts:
            mapper[i[0]] = i[1]
        f = open('mem.csv', 'w')
        writer = csv.writer(f)
        l = []
        for i in (Member._meta.get_fields()):
            l.append(i.name)
        writer.writerow(l)
        data = Member.objects.all().values_list()
        for s in data:
            s = list(s)
            writer.writerow(s)
        f.close()
        f = open('mem.csv', 'r')
        response = HttpResponse(f, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=Member.csv'
        return response




@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    actions = ['download_csv']
    readonly_fields = ('joined',)
    list_display = ('name', 'phone', 'email', 'organisation', 'joined')
    list_filter = ('district', 'joined',)

    def download_csv(self, request, queryset):
        options = districts
        mapper = {}
        for i in districts:
            mapper[i[0]] = i[1]
        f = open('stud.csv', 'w')
        writer = csv.writer(f)
        l = []
        for i in (Student._meta.get_fields()):
            l.append(i.name)
        writer.writerow(l)
        data = Student.objects.all().values_list()
        for s in data:
            s = list(s)
            writer.writerow(s)
        f.close()
        f = open('stud.csv', 'r')
        response = HttpResponse(f, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=Students.csv'
        return response

