from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=140)
    description = models.TextField()
    url = models.URLField(null=True, blank=True)
    picture = models.ImageField(upload_to='img/', blank=True)
    #slug?
    #priority so we can arrange this (use ordered model?)
    #boolean whether to show of not
    #my role
    #video

    # System fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['title']

# Class Client
# Class Agency
# Class Company
# Class Technolgy # maybe do as tags?