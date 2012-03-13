### -*- coding: utf-8 -*- ####################################################

from django.conf import settings
from native_tags.decorators import function

from ..models import Banner

def get_banner(slug, width, height, queryset=Banner.objects.all()):
    banner = queryset.get_or_create(slug=slug.encode('utf-8'))[0]
    return "banner_source.html", {
                'banner': banner, 'size': "%ix%i" % (width, height), 
                'width': width, 'height': height, 
                'STATIC_URL': settings.STATIC_URL,
    }

get_banner = function(get_banner, inclusion=True, cache=60)
