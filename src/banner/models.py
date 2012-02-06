### -*- coding: utf-8 -*- ####################################################

from django.db import models
from django.utils.translation import ugettext_lazy as _

from sorl.thumbnail.fields import ImageField 

from .utils import default_upload_to

class Banner(models.Model):

    slug = models.SlugField(_("Unique identifier"), unique=True)
    image = ImageField(_(u"Banner's image"), max_length=255, upload_to=default_upload_to, blank=True)
    link = models.CharField(_("External link"), max_length=255, blank=True, null=True)
    
    class Meta:
        ordering = ('slug',)
        verbose_name = _("banner")
        verbose_name_plural = _("banners")
    
    def __unicode__(self):
        return u"Banner: %s" % self.slug
