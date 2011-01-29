### -*- coding: utf-8 -*- ####################################################

from django.contrib.contenttypes.models import ContentType

def default_upload_to(instance, file_name):
    app_label, model = ContentType.objects.get_for_model(instance).natural_key()
    return 'uploads/%s/%s/%s_%s' % (app_label, model, instance.pk or '0', file_name)
