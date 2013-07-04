import datetime

from django.db import models
from django.utils.translation import ugettext_lazy as _

class FooItemBase(models.Model):
    """
    Foo item base.
    """
    title = models.CharField(_("Title"), max_length=100)
    slug = models.SlugField(_("Slug"), unique=True)
    body = models.TextField(_("Body"))
    date_published = models.DateTimeField(_("Date published"), blank=True, null=True, default=datetime.datetime.now())
    date_created = models.DateTimeField(_("Date created"), blank=True, null=True, auto_now_add=True, editable=False)
    date_updated = models.DateTimeField(_("Date updated"), blank=True, null=True, auto_now=True, editable=False)

    class Meta:
        abstract = True
        verbose_name = _("Foo item")
        verbose_name_plural = _("Foo items")

    def __unicode__(self):
        return self.title

class FooItem(FooItemBase):
    class Meta:
        verbose_name = _("Foo item")
        verbose_name_plural = _("Foo items")

class Foo2Item(FooItemBase):
    class Meta:
        verbose_name = _("Foo 2 item")
        verbose_name_plural = _("Foo 2 items")

class Foo3Item(FooItemBase):
    class Meta:
        verbose_name = _("Foo 3 item")
        verbose_name_plural = _("Foo 3 items")

class Foo4Item(FooItemBase):
    class Meta:
        verbose_name = _("Foo 4 item")
        verbose_name_plural = _("Foo 4 items")
