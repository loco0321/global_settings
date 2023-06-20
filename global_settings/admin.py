""" Module to define admin interfaces """
import json
from django.contrib import admin

from global_settings.models import GlobalSettings
from global_settings.utils import get_global_setting


class GlobalSettingsAdmin(admin.ModelAdmin):
    list_display = ('name', 'value', 'type', 'created_at')
    list_filter = ('type',)
    search_fields = ('name',)

    actions = ['test_formatted_value', 'indent_text_json']

    def test_formatted_value(self, request, queryset):
        for q in queryset:
            try:
                self.message_user(request, get_global_setting(q.name))
            except Exception as err:
                self.message_user(request, repr(err))

    def indent_text_json(self, request, queryset):
        for q in queryset:
            try:
                if q.type == q.DICT:
                    value = q.get_formatted_value()
                    q.value = json.dumps(value)
                    q.save()
                else:
                    self.message_user(request, u'Only dictionary type is able to indent.')
            except Exception as ex:
                self.message_user(request, u"Error: %s" % repr(ex))
            else:
                self.message_user(request, u'Successful update: %s' % q.value)


admin.site.register(GlobalSettings, GlobalSettingsAdmin)
