from django.db import models
from django.template.defaultfilters import slugify

class Project(models.Model):
    title = models.CharField(max_length=140)
    description = models.TextField()
    url = models.URLField(null=True, blank=True)
    video = models.URLField(null=True, blank=True)
    role = models.CharField(max_length=140, default='')
    technologies = models.CharField(max_length=140, default='')
    picture = models.ImageField(upload_to='img/', blank=True)
    slug = models.CharField(max_length=140, null=True)
    #priority so we can arrange this (use ordered model?)
    #boolean whether to show of not

    # System fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Project, self).save(*args, **kwargs)

    class Meta:
        ordering = ['title']

# Class Client
# Class Agency
# Class Company
# Class Technolgy # maybe do as tags?
