from django.db import models
from django.template.defaultfilters import slugify
import datetime

# Create your models here.
class Novel(models.Model):
    title = models.CharField(max_length = 200)
    author = models.CharField(max_length = 200)
    novel_slug = models.SlugField(unique=True, max_length = 300)
    def save(self, *args, **kwargs):
        if not self.id:
            self.novel_slug = slugify(self.title)
        super(Novel, self).save(*args, **kwargs)
    def __str__(self):
        return self.title

class Vol(models.Model):
    Novel = models.ForeignKey(Novel)
    title = models.CharField(max_length = 200)
    volNo = models.IntegerField(default = 1)
    def __str__(self):
        return self.title


class Chapter(models.Model):
    vol = models.ForeignKey(Vol)
    content = models.TextField()
    chapterNo = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('date pulished')
    chapter_slug = models.SlugField(unique=True, max_length = 300)
    def save(self, *args, **kwargs):
        if not self.id:
            nslug = self.vol.title + " Chapter " + self.chapterNo
            self.chapter_slug = slugify(nslug)
        super(Chapter, self).save(*args, **kwargs)
    def __str__(self):
        return self.chapterNo
