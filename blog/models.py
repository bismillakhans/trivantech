from django.db import models
from django.shortcuts import reverse
from taggit.managers import TaggableManager
from ckeditor.fields import RichTextField
from django_extensions.db.fields import AutoSlugField, ModificationDateTimeField

# Create your models here.
districts = (
    ('alp', 'Alappuzha'),
    ('ekm', 'Ernakulam'),
    ('idk', 'Idukki'),
    ('knr', 'Kannur'),
    ('ksr', 'Kasaragod'),
    ('kol', 'Kollam'),
    ('ktm', 'Kottayam'),
    ('koz', 'Kozhikode'),
    ('mpm', 'Malappuram'),
    ('pkd', 'Palakkad'),
    ('ptm', 'Pathanamthitta'),
    ('tvm', 'Thiruvananthapuram'),
    ('tcr', 'Thrissur'),
    ('wnd', 'Wayanad'),
)
positions = (
    ('Director', 'Director'),
    ('Chairman', 'Chairman'),
    ('Associate Director', 'Associate Director'),
    ('Secretary', 'Secretary'),
    ('Treasurer', 'Treasurer'),
    ('Member', 'Member'),
)
wtypes = (
    ('Workshops', 'Workshops'),
    ('Conferences', 'Conferences'),
    ('Seminars', 'Seminars'),
)
categories = (
    ('Statitics', 'Statitics'),
    ('Probabilty', 'Probabilty'),
    ('Algebra', 'Relational Algebra'),
    ('Geometry', 'Geometry'),
)


class Post(models.Model):
    title = models.CharField(max_length=70)
    slug = AutoSlugField(populate_from='title', overwrite=True)
    tags = TaggableManager()
    post_date = models.DateField(auto_now_add=True)
    post_update = ModificationDateTimeField()
    short_desc = models.TextField(max_length=250)
    img = models.ImageField(upload_to='img', blank=True,null=True)
    status = models.BooleanField(default=False, verbose_name="Approve Post")
    body = RichTextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post', args=[self.post_date.year, self.post_date.month, self.slug])


class Document(models.Model):
    file = models.FileField('Document', upload_to='mydocs/')
    fname = models.CharField(max_length=70)
    status = models.BooleanField(default=True, verbose_name="Status")
    category = models.CharField(
        max_length=40,
        choices=categories,
    )


class Link(models.Model):
    linkname = models.CharField(max_length=1000)
    name = models.CharField(max_length=70)
    status = models.BooleanField(default=True, verbose_name="Status")


class Work(models.Model):
    title = models.CharField(max_length=70)
    venue = models.CharField(max_length=70)
    status = models.BooleanField(default=True, verbose_name="Status")
    district = models.CharField(
        max_length=40,
        choices=districts,
    )
    sdate = models.DateTimeField()
    info = models.TextField()
    fdate = models.DateField()
    wtype = models.CharField(
        max_length=40,
        choices=wtypes,
    )





class Student(models.Model):
    name = models.CharField(max_length=100)
    district = models.CharField(
        max_length=40,
        choices=districts,
    )
    phone = models.CharField(max_length=10)
    email = models.EmailField(max_length=70, blank=True)
    organisation = models.CharField(max_length=250, verbose_name="Organization / Institution")
    address = models.TextField()
    joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Member(models.Model):
    name = models.CharField(max_length=100)
    rank = models.IntegerField(default=100)
    district = models.CharField(
        max_length=40,
        choices=districts,
    )
    position = models.CharField(
        max_length=30,
        choices=positions,
    )
    invigilation = models.CharField(max_length=250, verbose_name="Invigilation ")
    phone = models.CharField(max_length=10,blank=True)
    email = models.EmailField(max_length=70, blank=True)
    organisation = models.CharField(max_length=250, verbose_name="Organization / Institution")
    department = models.CharField(max_length=250, verbose_name="Department ")
    address = models.TextField()
    status = models.BooleanField(default=True, verbose_name="Status")
    joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Gallery(models.Model):
    title = models.CharField(max_length=70,null=True,blank=True)
    img = models.ImageField(upload_to='gallery', default="download.jpeg")
    status = models.BooleanField(default=True, verbose_name="Approve")
    g_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
