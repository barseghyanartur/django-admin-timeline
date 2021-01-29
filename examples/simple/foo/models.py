import datetime

from django.db import models
from django.utils.translation import gettext_lazy as _

import six


@six.python_2_unicode_compatible
class FooItemBase(models.Model):
    """Foo item base."""

    title = models.CharField(_("Title"), max_length=100)
    slug = models.SlugField(_("Slug"), unique=True)
    body = models.TextField(_("Body"))
    date_published = models.DateTimeField(_("Date published"), blank=True,
                                          null=True,
                                          default=datetime.datetime.now())
    date_created = models.DateTimeField(_("Date created"), blank=True,
                                        null=True, auto_now_add=True,
                                        editable=False)
    date_updated = models.DateTimeField(_("Date updated"), blank=True,
                                        null=True, auto_now=True,
                                        editable=False)

    class Meta(object):
        """Options."""

        abstract = True
        verbose_name = _("Foo item")
        verbose_name_plural = _("Foo items")

    def __str__(self):
        return self.title


class FooItem(FooItemBase):
    """FooItem."""

    class Meta(object):
        """Meta."""

        verbose_name = _("Foo item")
        verbose_name_plural = _("Foo items")


class Foo2Item(FooItemBase):
    """Foo2Item."""

    class Meta(object):
        """Meta."""

        verbose_name = _("Foo 2 item")
        verbose_name_plural = _("Foo 2 items")


class Foo3Item(FooItemBase):
    """Foo3Item."""

    class Meta(object):
        """Meta."""

        verbose_name = _("Foo 3 item")
        verbose_name_plural = _("Foo 3 items")


class Foo4Item(FooItemBase):
    """Foo4Item."""

    class Meta(object):
        """Meta."""

        verbose_name = _("Foo 4 item")
        verbose_name_plural = _("Foo 4 items")
