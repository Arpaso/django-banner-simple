### -*- coding: utf-8 -*- ####################################################


from django.contrib import admin

from sorl.thumbnail.admin import AdminImageMixin

from .models import Banner

class BannerAdmin(AdminImageMixin, admin.ModelAdmin):

    list_display = ('slug', 'link')
    search_fields = ('slug', 'link')


admin.site.register(Banner, BannerAdmin)
