from django.db import models


# Create your models here.
class Background(models.Model):
    '''
    Used to store data about the Background
    '''
    url = models.URLField(null=True, blank=True);
    color=models.CharField(null=True, blank=True, max_length=7);

    def __str__(self):
        if self.color == '':
            return '{url}'.format(url = self.url);
        else:
            return '{color}'.format(color = self.color);
        
    def __unicode__(self):
        if self.color == '':
            return '{url}'.format(url = self.url);
        else:
            return '{color}'.format(color = self.color);


class TimelineEvent(models.Model):
    '''
    Models an Event that appears on Emperitas Timeline
    '''
    start_date = models.DateField(null=True, blank=True);
    end_date = models.DateField(null=True, blank=True);
    display_date = models.CharField(null=True, blank=True, max_length=75);
    headline = models.CharField(null=False, max_length=75);
    text = models.TextField(null=True, blank=True);
    media = models.URLField(null=True, blank=True);
    media_credit = models.CharField(null=True, blank=True, max_length=75);
    media_caption = models.CharField(null=True, blank=True, max_length=140);
    media_thumbnail = models.URLField(null=True, blank=True);
    slide_type = models.CharField(null=True, blank=True, max_length=30);
    group = models.CharField(null=True, blank=True, max_length=75);
    background = models.ForeignKey('Background',on_delete=models.CASCADE, null=True, blank=True);

    def __str__(self):
        return '{headline}'.format(headline = self.headline);
    
    def __unicode__(self):
        return '{headline}'.format(headline = self.headline);
