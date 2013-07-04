from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from foo.models import FooItem, Foo2Item, Foo3Item, Foo4Item


class FooItemBaseAdmin(admin.ModelAdmin):
    """
    Foo item admin.
    """
    list_display = ('title', 'date_published')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('date_published',)
    readonly_fields = ('date_created', 'date_updated',)

    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'body',)
        }),
        (_("Publication date"), {
            'classes': ('',),
            'fields': ('date_published',)
        }),
        (_("Additional"), {
            'classes': ('collapse',),
            'fields': ('date_created', 'date_updated') #,
        })
    )

    class Meta:
        app_label = _('Foo item')


class FooItemAdmin(FooItemBaseAdmin):
    class Meta:
        app_label = _('Foo item')

admin.site.register(FooItem, FooItemAdmin)


class Foo2ItemAdmin(FooItemBaseAdmin):
    class Meta:
        app_label = _('Foo 2 item')

admin.site.register(Foo2Item, Foo2ItemAdmin)


class Foo3ItemAdmin(FooItemBaseAdmin):
    class Meta:
        app_label = _('Foo 3 item')

admin.site.register(Foo3Item, Foo3ItemAdmin)


class Foo4ItemAdmin(FooItemBaseAdmin):
    class Meta:
        app_label = _('Foo 4 item')

admin.site.register(Foo4Item, Foo4ItemAdmin)
