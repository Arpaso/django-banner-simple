### -*- coding: utf-8 -*- ####################################################

from django.conf import settings
from django import template
from banner.models import Banner

register = template.Library()

@register.inclusion_tag('banner_source.html')
def get_banner(slug, width, height, queryset=Banner.objects.all()):
    banner = queryset.get_or_create(slug=slug.encode('utf-8'))[0]
    return {
        'banner': banner, 'size': "%ix%i" % (width, height), 
        'width': width, 'height': height, 
        'STATIC_URL': settings.STATIC_URL,
    }
