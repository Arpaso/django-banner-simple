Django simple banner template tag
=================================

Link to repository: https://github.com/Arpaso/django-banner-simple

Provides new template tag to display banner uploaded via admin interface.

**Banner** model and **BannerAdmin** is added.

Usage
=====

* You have to use south migrations to update your database::

    python manage.py migrate

.. NOTE:: Banner admin page is provided for adding banner through django admin interface


* Add application to INSTALLED_APPS in settings.py::

    ...
    'banner',
    ...

* Use template tag in your templates as is::

    {% get_banner 'banner_name' 150 150 %}


.. NOTE:: get_banner(slug, width, height, queryset=Banner.objects.all())

Uses also settings.STATIC_URL to display banner image.





