### -*- coding: utf-8 -*- ####################################################


from django.contrib import admin

from sorl.thumbnail.admin import AdminImageMixin

from .models import Banner, AlternativeImage

class AlternativeInline(AdminImageMixin, admin.TabularInline):
    model = AlternativeImage
    extra = 0

class BannerAdmin(AdminImageMixin, admin.ModelAdmin):

    list_display = ('slug', 'link')
    search_fields = ('slug', 'link')
    inlines = (AlternativeInline,)

admin.site.register(Banner, BannerAdmin)
