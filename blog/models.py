from django.db import models
from django.shortcuts import reverse
from taggit.managers import TaggableManager
from ckeditor.fields import RichTextField
from django_extensions.db.fields import AutoSlugField, ModificationDateTimeField

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=70)
    slug = AutoSlugField(populate_from='title', overwrite=True)
    tags = TaggableManager()
    post_date = models.DateField(auto_now_add=True)
    post_update = ModificationDateTimeField()
    short_desc = models.TextField(max_length=250)
    status = models.BooleanField(default=True, verbose_name="Approve Post")
    body = RichTextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post', args=[self.post_date.year, self.post_date.month, self.slug])