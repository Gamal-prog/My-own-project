from django.db import models
from django.conf import settings
from imagekit.models import ImageSpecField 
from pilkit.processors import Thumbnail 

class Photo(models.Model):
    title = models.CharField(max_length=100, blank=False)
    discription = models.CharField(max_length=500, blank=False)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uplouds/pictures')
    published_date = models.DateTimeField(blank=True, null=True)

    image_thumbnail = ImageSpecField(source='image',
                                    processors=[Thumbnail(70, 50)],
                                    format='JPEG',
                                    options={'quality': 60})
    
    def __str__(self):
        template = '{0.author} {0.title}'
        return template.format(self)